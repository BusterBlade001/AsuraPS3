import glob

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "func_0098A674" in txt or "func_009919E8" in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if ("func_0098A674" in l or "func_009919E8" in l) and "function_table" not in l and not l.startswith("void "):
                print(f"\n=== Match in {p.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-25), min(len(lines), i+30)):
                    print(f"{j+1:06d}: {lines[j]}")
