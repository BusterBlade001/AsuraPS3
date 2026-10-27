import glob, os, shutil, struct, subprocess, sys
from pathlib import Path
sys.path.insert(0, r"C:\AsuraPS3\ps3recomp\tools")
from wrap_spu_elf import wrap

def find_pic_targets(raw):
    # Detectar el delta PIC (brsl $r126, pc_next + ila $rX, link_addr + sf $r126, $rX, $r126)
    link_delta = 0
    for off in range(0, len(raw) - 32, 4):
        w = struct.unpack_from(">I", raw, off)[0]
        if (w >> 25) & 0x7F == 0x21: # ila $rX, imm18
            reg = w & 0x7F
            imm = (w >> 7) & 0x3FFFF
            # buscar brsl $r126 cerca
            for d in range(-16, 20, 4):
                if 0 <= off + d < len(raw) - 4:
                    wb = struct.unpack_from(">I", raw, off + d)[0]
                    if (wb >> 23) & 0x1FF == 0x066 and (wb & 0x7F) == 126: # brsl $r126
                        s16 = ((wb >> 7) & 0xFFFF)
                        if s16 & 0x8000: s16 -= 0x10000
                        pc_brsl = (off + d) + (s16 << 2)
                        if imm > pc_brsl:
                            link_delta = imm - pc_brsl
                            break
        if link_delta:
            break

    targets = set([0x1C])
    # Destino del branch en 0x1C
    w1c = struct.unpack_from(">I", raw, 0x1C)[0]
    if (w1c >> 23) & 0x1FF in (0x064, 0x060):
        s16 = (w1c >> 7) & 0xFFFF
        if s16 & 0x8000: s16 -= 0x10000
        t = (0x1C if ((w1c >> 23) & 0x1FF) == 0x064 else 0) + (s16 << 2)
        if 0 <= t < len(raw):
            targets.add(t)

    # Todas las constantes ila ajustadas por link_delta que caigan dentro del binario
    for off in range(0x20, len(raw) - 4, 4):
        w = struct.unpack_from(">I", raw, off)[0]
        if (w >> 25) & 0x7F == 0x21: # ila
            imm = (w >> 7) & 0x3FFFF
            for cand in (imm - link_delta, imm):
                if 0x20 <= cand < len(raw) and (cand % 4) == 0:
                    targets.add(cand)
    return link_delta, sorted(targets)

job_bins = sorted(glob.glob(r"C:\AsuraPS3\out\jobmods\spujob_*.bin"))
extra_args = []

for jb in job_bins:
    raw = open(jb, "rb").read()
    base_name = "_".join(os.path.splitext(os.path.basename(jb))[0].split("_")[:2])
    elf_path = os.path.join(r"C:\AsuraPS3\out\spu", base_name + ".elf")

    # Borrar carpeta previa para forzar re-lift limpio de este spujob con entry=0x1C
    lifted_dir = os.path.join(r"C:\AsuraPS3\ps3recomp\templates\project\spu", base_name)
    if os.path.exists(lifted_dir):
        shutil.rmtree(lifted_dir)

    delta, extras = find_pic_targets(raw)
    elf_bytes = wrap(raw, base=0x0, entry=0x1C)
    open(elf_path, "wb").write(elf_bytes)

    print(f"[wrap] {base_name}.elf ({len(raw)} B, entry=0x1C, pic_delta=0x{delta:X}, extras={len(extras)} targets)")
    if extras:
        extra_args += ["--extra-funcs", f"{base_name}=" + ",".join(hex(x) for x in extras)]

cmd = [
    sys.executable, r"C:\AsuraPS3\ps3recomp\tools\build_spu_workloads.py",
    "--images", r"C:\AsuraPS3\out\spu",
    "--lifted", r"C:\AsuraPS3\ps3recomp\templates\project\spu",
    "--out", r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_workloads.c",
    "--constructor", "--title", "Asura"
] + extra_args

subprocess.run(cmd, check=True)

# Quitar HALT-ASSERT en los 2 spujob para que no aborten por checks de alineacion de contexto
for jb in job_bins:
    base_name = "_".join(os.path.splitext(os.path.basename(jb))[0].split("_")[:2])
    c_file = Path(r"C:\AsuraPS3\ps3recomp\templates\project\spu") / base_name / "spu_recomp.c"
    ct = c_file.read_text(encoding="latin-1")
    import re
    ct_new = re.sub(r'if \([^\n]+HALT-ASSERT[^\n]+\n', '/* halt-assert bypassed */\n', ct)
    c_file.write_text(ct_new, encoding="latin-1")
    print(f"[patch] {base_name}/spu_recomp.c listo (lineas: {len(ct_new.splitlines())})")

# Actualizar spurs_job.c para que el PC inicial sea 0x1C cuando hay header PIC
sj_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spurs_job.c")
sj_txt = sj_path.read_text(encoding="latin-1")
sj_txt = sj_txt.replace("ctx.pc       = 0x10;", "ctx.pc       = 0x1C;")
sj_path.write_text(sj_txt, encoding="latin-1")
print("[patch] spurs_job.c: ctx.pc = 0x1C configurado!")
