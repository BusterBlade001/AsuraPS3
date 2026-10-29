from collections import Counter
import re

path = r"C:\AsuraPS3\out\boot41.log"
lines = [l.strip() for l in open(path, "r", encoding="latin-1") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT41.LOG: {len(lines)} ===")

print("\n--- 1. TOP 15 MENSAJES MAS REPETIDOS EN BOOT41.LOG ---")
norm = [re.sub(r"0x[0-9A-Fa-f]+|\d+", "N", l)[:100] for l in lines]
for msg, cnt in Counter(norm).most_common(15):
    print(f"  [{cnt:6d}x] {msg}")

print("\n--- 2. ULTIMOS 35 EVENTOS DE ARCHIVOS / SHADERS / VIDEOS ---")
ev = [f"[{i:05d}] {l}" for i, l in enumerate(lines) if any(k in l for k in ("[fs]", "[sys_fs]", "[FP]", "[VP]", ".BIK", ".XXX", "FAIL", "ERROR", "CRASH", "spu-spin", "STALL", "unresolved"))]
for l in ev[-35:]:
    print(" ", l[:115])

print("\n--- 3. ULTIMAS 25 LINEAS DEL LOG ---")
for l in lines[-25:]:
    print(" ", l[:115])
