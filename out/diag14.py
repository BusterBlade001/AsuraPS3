from collections import Counter
import re

path = r"C:\AsuraPS3\out\boot14.log"
lines = [l.strip() for l in open(path, "r", encoding="utf-8", errors="replace") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT14.LOG: {len(lines)} ===")

print("\n--- 1. TOP 15 MENSAJES MAS REPETIDOS EN BOOT14.LOG (CAUSA DE LOS 10 FPS) ---")
norm_lines = [re.sub(r"0x[0-9A-Fa-f]+|\d+", "N", l)[:100] for l in lines]
for msg, cnt in Counter(norm_lines).most_common(15):
    print(f"  [{cnt:6d}x] {msg}")

print("\n--- 2. ARCHIVOS .BIK ABIERTOS Y ULTIMAS 20 LINEAS ---")
for i, l in enumerate(lines):
    if ".BIK" in l.upper() or "[FP]" in l or "ERROR" in l or "CRASH" in l:
        print(f"  [{i:05d}] {l[:110]}")
print("  --- Tail ---")
for l in lines[-15:]:
    print(" ", l[:110])

d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="utf-8", errors="ignore").splitlines()
print("\n--- 3. rsx_d3d12_backend.c: QUADS (6070..6155) Y FP DECOMPILER (1980..2090) ---")
for j in range(6070, 6155):
    print(f"{j+1:04d}: {d3d[j]}")
for j in range(1980, 2090):
    print(f"{j+1:04d}: {d3d[j]}")
