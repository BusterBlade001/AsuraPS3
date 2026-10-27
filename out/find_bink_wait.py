import glob

# 1. Ver 0x014ACC58 en ppu_recomp_060.cpp (lineas 116815..116900)
l60 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_060.cpp", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. TrophyInfo en 0x014ACC58 (ppu_recomp_060.cpp:116815..116895) ===")
for j in range(116815, min(len(l60), 116895)):
    print(f"{j+1:06d}: {l60[j]}")

# 2. Buscar 0x008BE940 / func_00D238CC (MainThread) y 0x00889120 / func_002BEC24 (RenderingThread)
targets = ["0x008BE940", "void func_00D238CC(", "0x00889120", "void func_002BEC24("]
for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    for t in targets:
        if t in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if t in l:
                    print(f"\n=== Match {t} in {p.split('\\')[-1]}:{i+1} ===")
                    start = max(0, i-20) if t.startswith("0x") else i
                    for j in range(start, min(len(lines), start+55)):
                        print(f"{j+1:06d}: {lines[j]}")
                    break

# 3. Ver cómo traduce rutas runtime/syscalls/sys_fs.c
sfs = open(r"C:\AsuraPS3\ps3recomp\runtime\syscalls\sys_fs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== 3. runtime/syscalls/sys_fs.c (primeras 120 lineas) ===")
for j in range(0, min(len(sfs), 120)):
    print(f"{j+1:04d}: {sfs[j]}")
