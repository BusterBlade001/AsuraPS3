import glob, re

files = sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp"))

targets = ["func_00899040", "func_00899168", "0x0089B3AC", "0x0089B3C8", "func_008A9458"]

for path in files:
    txt = open(path, "r", encoding="utf-8", errors="ignore").read()
    for t in targets:
        if t in txt:
            lines = txt.splitlines()
            for i, line in enumerate(lines):
                if (t.startswith("func_") and f"void {t}(" in line) or (t.startswith("0x") and t in line):
                    print(f"\n=== MATCH {t} in {path.split('\\')[-1]}:{i+1} ===")
                    start = max(0, i - 25) if t.startswith("0x") else i
                    end = min(len(lines), i + 120)
                    for j in range(start, end):
                        print(f"{j+1:06d}: {lines[j]}")
                        if j > i and lines[j].startswith("void func_"):
                            break
                    break
