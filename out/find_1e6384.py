import glob

lines = [l.strip() for l in open(r"C:\AsuraPS3\out\boot33.log", "r", encoding="latin-1") if l.strip()]
print("=== 1. Lineas 46350..46470 de boot33.log ===")
for i in range(46350, min(len(lines), 46470)):
    print(f"[{i:05d}] {lines[i][:120]}")

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    if "0x001E6384" in txt:
        plines = txt.splitlines()
        for i, l in enumerate(plines):
            if "0x001E6384" in l:
                print(f"\n=== 2. Codigo PPU en 0x001E6384 ({p.split('\\')[-1]}:{i+1}) ===")
                for j in range(max(0, i-35), min(len(plines), i+25)):
                    print(f"{j+1:06d}: {plines[j]}")
                break
