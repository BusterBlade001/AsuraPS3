import glob

# 1. Ver el código alrededor de func_009A43A4 (QueuePop bloqueante) en ppu_recomp_029.cpp
l29 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp", "r", encoding="latin-1").read().splitlines()
print("=== 1. Llamadores de cellSpursQueuePopBody (func_01606818) ===")
for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    if "func_01606818" in txt:
        pl = txt.splitlines()
        for i, l in enumerate(pl):
            if "func_01606818" in l and not l.startswith("void ") and "function_table" not in l:
                print(f"\n--- {p.split('\\')[-1]}:{i+1} ---")
                for j in range(max(0, i-20), min(len(pl), i+30)):
                    print(f"{j+1:06d}: {pl[j]}")

# 2. Ver [cri] REAL SpursTasksetContext en runtime/spu/spu_workload.c
wl = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(wl):
    if "REAL SpursTasksetContext" in l:
        print(f"\n=== 2. spu_workload.c:{i+1} ===")
        for j in range(max(0, i-25), min(len(wl), i+30)):
            print(f"{j+1:04d}: {wl[j]}")
        break

# 3. Ver 0x0D310 y 0x1FCC0 en spu_0021_at_018ECF00 (img=22)
p21 = open(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0021_at_018ECF00\spu_recomp.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(p21):
    if "d310" in l.lower() or "void spu_0021_at_018ecf00_spu_func_0001fcc0(" in l.lower():
        print(f"\n=== 3. spu_0021 (img=22) linea {i+1} ===")
        for j in range(max(0, i-25), min(len(p21), i+35)):
            print(f"{j+1:05d}: {p21[j]}")
