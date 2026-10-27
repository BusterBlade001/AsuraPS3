import glob

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "func_00998C28" in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "func_00998C28" in l and not l.startswith("void ") and "function_table" not in l:
                print(f"\n=== CALLER OF func_00998C28 in {p.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-40), min(len(lines), i+80)):
                    print(f"{j+1:06d}: {lines[j]}")
