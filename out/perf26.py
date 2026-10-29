from collections import Counter
import re

path = r"C:\AsuraPS3\out\boot26.log"
lines = [l.strip() for l in open(path, "r", encoding="latin-1") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT26.LOG: {len(lines)} ===")

print("\n--- 1. TOP 20 MENSAJES MAS REPETIDOS EN BOOT26.LOG ---")
norm = [re.sub(r"0x[0-9A-Fa-f]+|\d+", "N", l)[:100] for l in lines]
for msg, cnt in Counter(norm).most_common(20):
    print(f"  [{cnt:6d}x] {msg}")

print("\n--- 2. ULTIMAS 35 LINEAS DISTINTAS EN EL MENU ---")
prev = None
tail = []
for l in reversed(lines):
    if l != prev:
        tail.append(l[:115])
        prev = l
    if len(tail) >= 35:
        break
for l in reversed(tail):
    print(" ", l)
