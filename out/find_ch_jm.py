ch = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_channels.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. spu_channels.c (2380..2450) ===")
for j in range(2380, min(len(ch), 2450)):
    print(f"{j+1:04d}: {ch[j]}")

jm = open(r"C:\AsuraPS3\ps3recomp\tools\lift_jobmods.py", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== 2. tools/lift_jobmods.py (primeras 90 lineas) ===")
for j in range(0, min(len(jm), 90)):
    print(f"{j+1:04d}: {jm[j]}")
