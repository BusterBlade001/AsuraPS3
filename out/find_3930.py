p0 = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0000_at_017AA900\spu_recomp.c"
l0 = open(p0, "r", encoding="utf-8", errors="ignore").read().splitlines()

for idx, line in enumerate(l0):
    if "3930" in line.lower() or "void spu_0000_at_017aa900_spu_func_000163f0(" in line.lower():
        print(f"\n=== Match in spu_0000:{idx+1} ===")
        for j in range(max(0, idx-25), min(len(l0), idx+55)):
            print(f"{j+1:05d}: {l0[j]}")

import glob
for p in glob.glob(r"C:\AsuraPS3\ps3recomp\runtime\spu\*.c*"):
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "branched into unlifted LS" in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "branched into unlifted LS" in l:
                print(f"\n=== {p.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-25), min(len(lines), i+35)):
                    print(f"{j+1:04d}: {lines[j]}")
