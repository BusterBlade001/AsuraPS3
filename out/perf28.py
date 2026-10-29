from collections import Counter
import re

path = r"C:\AsuraPS3\out\boot28.log"
lines = [l.strip() for l in open(path, "r", encoding="latin-1") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT28.LOG: {len(lines)} ===")

print("\n--- 1. LINEAS DE TIEMPO GPU/CPU ([PERF] / [DRAIN]) ---")
perf_lines = [l for l in lines if any(k in l for k in ("PERF", "ms", "wait", "WAIT", "SEMA", "timeout", "park", "stuck", "circle"))]
for l in perf_lines[-35:]:
    print(" ", l[:120])

print("\n--- 2. TOP 20 MENSAJES MAS FRECUENTES EN BOOT28.LOG ---")
norm = [re.sub(r"0x[0-9A-Fa-f]+|\d+", "N", l)[:100] for l in lines]
for msg, cnt in Counter(norm).most_common(20):
    print(f"  [{cnt:6d}x] {msg}")

d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(d3d):
    if "perf_on()" in l:
        print(f"\n--- 3. Medicion perf_on() en rsx_d3d12_backend.c:{i+1} ---")
        for j in range(max(0, i-5), min(len(d3d), i+25)):
            print(f"{j+1:04d}: {d3d[j]}")
