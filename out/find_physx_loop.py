import glob

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    for fn in ["func_00A6672C", "func_00A666D4", "func_00A6669C"]:
        if fn in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if fn in l and not l.startswith("void ") and "function_table" not in l:
                    print(f"\n=== Call {fn} in {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(max(0, i-25), min(len(lines), i+35)):
                        print(f"{j+1:06d}: {lines[j]}")
