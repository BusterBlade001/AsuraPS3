import glob, os, subprocess, sys
sys.path.insert(0, r"C:\AsuraPS3\ps3recomp\tools")
from wrap_spu_elf import wrap
from lift_jobmods import manual_link_targets, switch_table_targets

job_bins = sorted(glob.glob(r"C:\AsuraPS3\out\jobmods\spujob_*.bin"))
extra_args = []

for jb in job_bins:
    raw = open(jb, "rb").read()
    # Nombre limpio sin el tamaño al final: spujob_42E1FC8CEE0BE246
    base_name = "_".join(os.path.splitext(os.path.basename(jb))[0].split("_")[:2])
    elf_path = os.path.join(r"C:\AsuraPS3\out\spu", base_name + ".elf")

    # Detectar entry (0x10 tras cabecera PIC de 4x ila $r2, o 0x0)
    w0 = int.from_bytes(raw[0:4], "big")
    entry = 0x10 if ((w0 >> 25) & 0x7F) == 0x21 and (w0 & 0x7F) == 2 else 0x0

    elf_bytes = wrap(raw, base=0x0, entry=entry)
    open(elf_path, "wb").write(elf_bytes)

    extras = sorted(set(manual_link_targets(raw, base=0x0) + switch_table_targets(raw, base=0x0)))
    print(f"[wrap] {base_name}.elf ({len(raw)} B, base=0x0, entry=0x{entry:X}, extras={[hex(x) for x in extras]})")
    if extras:
        extra_args += ["--extra-funcs", f"{base_name}=" + ",".join(hex(x) for x in extras)]

cmd = [
    sys.executable, r"C:\AsuraPS3\ps3recomp\tools\build_spu_workloads.py",
    "--images", r"C:\AsuraPS3\out\spu",
    "--lifted", r"C:\AsuraPS3\ps3recomp\templates\project\spu",
    "--out", r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_workloads.c",
    "--constructor", "--title", "Asura"
] + extra_args

print("Running:", " ".join(cmd))
subprocess.run(cmd, check=True)
