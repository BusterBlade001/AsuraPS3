import re
path = r"C:\AsuraPS3\out\boot.log"
raw = open(path, "rb").read().replace(b"\x00", b"").decode("utf-8", errors="replace")
lines = [l.strip() for l in raw.splitlines() if l.strip()]

prev_norm = None
shown = 0
for i, l in enumerate(lines[175:], start=175):
    if any(k in l for k in ("SetPrepareFlip", "SetFlipImmediate", "timer_usleep")):
        continue
    if "ProgressBar[0] =" in l and not (l.endswith("= 1%") or l.endswith("= 100%")):
        continue
    # Normalizar timestamps t=12345us para no repetir la misma linea
    norm = re.sub(r"t=\d+us", "t=X", l)
    if norm != prev_norm:
        print(f"[{i:05d}] {l}")
        prev_norm = norm
        shown += 1
        if shown >= 200:
            print("... (truncado a 200 eventos) ...")
            break
