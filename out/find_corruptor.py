import glob, struct

# 1. Ver los segmentos PT_LOAD del EBOOT.ELF
elf = open(r"C:\AsuraPS3\game\PS3_GAME\USRDIR\EBOOT.ELF", "rb").read()
e_phoff = struct.unpack_from(">Q", elf, 32)[0]
e_phnum = struct.unpack_from(">H", elf, 56)[0]
print("=== 1. Segmentos PT_LOAD de EBOOT.ELF ===")
for i in range(e_phnum):
    p_type, p_flags, p_offset, p_vaddr, p_paddr, p_filesz, p_memsz, p_align = struct.unpack_from(">IIQQQQQQ", elf, e_phoff + i * 56)
    if p_type == 1:
        print(f"  PT_LOAD[{i}]: vaddr=0x{p_vaddr:08X}..0x{p_vaddr+p_memsz:08X} filesz=0x{p_filesz:X} flags=0x{p_flags:X}")

# 2. Ver lineas 51550..51678 de boot41.log
lines = [l.strip() for l in open(r"C:\AsuraPS3\out\boot41.log", "r", encoding="latin-1") if l.strip()]
print("\n=== 2. Lineas 51550..51678 de boot41.log ===")
for i in range(51550, min(len(lines), 51678)):
    print(f"[{i:05d}] {lines[i][:120]}")

# 3. Ver 0x00B8E788 y 0x00B8E234 en el codigo PPU
for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    if "0x00B8E788" in txt or "0x00B8E234" in txt:
        pl = txt.splitlines()
        for i, l in enumerate(pl):
            if "0x00B8E788" in l or "0x00B8E234" in l:
                print(f"\n=== 3. Match en {p.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-25), min(len(pl), i+20)):
                    print(f"{j+1:06d}: {pl[j]}")
