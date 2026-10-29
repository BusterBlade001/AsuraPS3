import glob, struct

elf = open(r"C:\AsuraPS3\game\PS3_GAME\USRDIR\EBOOT.ELF", "rb").read()
e_phoff = struct.unpack_from(">Q", elf, 32)[0]
e_phnum = struct.unpack_from(">H", elf, 56)[0]

opd_va = 0x01997000
func_va = 0
for i in range(e_phnum):
    p_type, p_flags, p_offset, p_vaddr, p_paddr, p_filesz, p_memsz, p_align = struct.unpack_from(">IIQQQQQQ", elf, e_phoff + i * 56)
    if p_type == 1 and p_vaddr <= opd_va < p_vaddr + p_filesz:
        off = p_offset + (opd_va - p_vaddr)
        func_va, toc_va = struct.unpack_from(">II", elf, off)
        print(f"OPD 0x{opd_va:08X} -> func_0x{func_va:08X} (TOC=0x{toc_va:08X})")
        break

target_fn = f"void func_{func_va:08X}("
for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    if target_fn in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if target_fn in l:
                print(f"\n=== {target_fn} en {p.split('\\')[-1]}:{i+1} ===")
                for j in range(i, min(len(lines), i+95)):
                    print(f"{j+1:06d}: {lines[j]}")
                break
