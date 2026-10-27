from collections import Counter

path = r"C:\AsuraPS3\out\boot.log"
with open(path, "r", encoding="utf-8", errors="replace") as f:
    lines = [line.rstrip("\r\n") for line in f if line.strip()]

print(f"=== TOTAL LINEAS EN BOOT.LOG: {len(lines)} ===\n")

print("--- 1. PRIMERAS 55 LINEAS (ARRANQUE) ---")
for l in lines[:55]:
    print(l)

print("\n--- 2. TRANSICION ALREDEDOR DEL 100% DE LA BARRA DE PROGRESO ---")
idx_100 = next((i for i, l in enumerate(lines) if "100" in l and ("progress" in l.lower() or "dialog" in l.lower() or "%" in l)), None)
if idx_100 is not None:
    start = max(0, idx_100 - 15)
    end = min(len(lines), idx_100 + 45)
    prev = None
    for i in range(start, end):
        if lines[i] != prev:
            print(f"[{i}] {lines[i]}")
            prev = lines[i]
else:
    print("(No se encontró línea literal con '100', mostrando líneas únicas intermedias)")
    seen = set()
    for i, l in enumerate(lines[55:]):
        if l not in seen:
            seen.add(l)
            print(f"[{i+55}] {l}")
            if len(seen) >= 50:
                break

print("\n--- 3. TOP 30 MENSAJES / ERRORES MAS REPETIDOS ---")
counts = Counter(lines)
for line, count in counts.most_common(30):
    print(f"[{count:6d}x] {line[:140]}")

print("\n--- 4. ULTIMAS 40 LINEAS DISTINTAS AL FINAL DEL LOG ---")
tail_unique = []
for l in reversed(lines):
    if not tail_unique or l != tail_unique[-1]:
        tail_unique.append(l)
    if len(tail_unique) >= 40:
        break
for l in reversed(tail_unique):
    print(l)
