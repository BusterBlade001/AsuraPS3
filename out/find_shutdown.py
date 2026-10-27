import glob

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "func_01604358" not in txt:
        continue
    lines = txt.splitlines()
    for i, l in enumerate(lines):
        if "func_01604358" in l and not l.startswith("void func_01604358") and "function_table" not in l:
            print(f"\n=== CALLER OF func_01604358 (ShutdownTaskset) in {p.split('\\')[-1]}:{i+1} ===")
            for j in range(max(0, i-45), min(len(lines), i+25)):
                print(f"{j+1:06d}: {lines[j]}")
