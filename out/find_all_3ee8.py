import glob

print("=== 1. Registro en spu_workloads.c ===")
print(open(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_workloads.c", "r", encoding="latin-1").read())

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\spu\*\spu_recomp.c")):
    txt = open(p, "r", encoding="latin-1").read()
    if "3ee8" in txt.lower():
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "3ee8" in l.lower():
                print(f"\n=== 2. Match 3EE8 in {p.split('\\')[-2]}:{i+1} ===")
                for j in range(max(0, i-40), min(len(lines), i+20)):
                    print(f"{j+1:05d}: {lines[j]}")
