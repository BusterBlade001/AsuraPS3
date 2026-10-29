wl = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c", "r", encoding="latin-1").read().splitlines()
print("=== 1. spu_workload.c (780..855) ===")
for j in range(780, min(len(wl), 855)):
    print(f"{j+1:04d}: {wl[j]}")

p21 = open(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0021_at_018ECF00\spu_recomp.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(p21):
    if "09c9c" in l.lower() or "9c9c" in l.lower() or "void spu_0021_at_018ecf00_spu_func_00006d" in l.lower():
        print(f"\n=== 2. spu_0021 (img=22) linea {i+1} ===")
        for j in range(max(0, i-35), min(len(p21), i+25)):
            print(f"{j+1:05d}: {p21[j]}")
