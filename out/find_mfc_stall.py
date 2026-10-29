import glob

for p in glob.glob(r"C:\AsuraPS3\ps3recomp\runtime\spu\*.c*"):
    txt = open(p, "r", encoding="latin-1").read()
    if "[mfc-list] STALL" in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "[mfc-list] STALL" in l:
                print(f"=== 1. [mfc-list] STALL en {p.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-30), min(len(lines), i+40)):
                    print(f"{j+1:04d}: {lines[j]}")
                break

b35 = [l.strip() for l in open(r"C:\AsuraPS3\out\boot35.log", "r", encoding="latin-1") if l.strip()]
print("\n=== 2. Lineas 54325..54559 de boot35.log ===")
for i in range(54325, min(len(b35), 54560)):
    print(f"[{i:05d}] {b35[i][:120]}")
