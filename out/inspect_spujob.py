wl = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. spu_workload.c (740..885) ===")
for j in range(740, min(len(wl), 885)):
    print(f"{j+1:04d}: {wl[j]}")

wrap = open(r"C:\AsuraPS3\ps3recomp\tools\wrap_spu_elf.py", "r", encoding="utf-8", errors="ignore").read()
print("\n=== 2. tools/wrap_spu_elf.py ===")
print(wrap)

b16 = open(r"C:\AsuraPS3\out\boot16.log", "r", encoding="utf-8", errors="replace").read().splitlines()
print("\n=== 3. Ultimas 25 lineas de boot16.log ===")
for l in b16[-25:]:
    print(l)
