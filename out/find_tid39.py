import glob

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    if "0x00158604" in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "0x00158604" in l:
                print(f"=== 0x00158604 en {p.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-35), min(len(lines), i+40)):
                    print(f"{j+1:06d}: {lines[j]}")
                break

b35 = [l.strip() for l in open(r"C:\AsuraPS3\out\boot35.log", "r", encoding="latin-1") if l.strip()]
for l in b35:
    if "tid=39" in l:
        print("LOG tid=39:", l[:115])
