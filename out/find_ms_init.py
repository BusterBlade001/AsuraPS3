import glob
files = sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp"))
for p in files:
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    for target in ["0x0098AAFC", "0xA789E631"]:
        if target.lower() in txt.lower():
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if target.lower() in l.lower():
                    print(f"\n=== Match {target} in {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(max(0, i-25), min(len(lines), i+25)):
                        print(f"{j+1:06d}: {lines[j]}")
