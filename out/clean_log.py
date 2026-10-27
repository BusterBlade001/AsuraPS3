path = r"C:\AsuraPS3\out\boot.log"
raw = open(path, "rb").read().replace(b"\x00", b"").decode("utf-8", errors="replace")
lines = [l.strip() for l in raw.splitlines() if l.strip()]

print(f"Total lineas limpias: {len(lines)}\n")

prev = None
shown = 0
for i, l in enumerate(lines):
    # Filtrar el spam de flips y pasos intermedios de la barra (dejamos 1% y 100%)
    if "SetPrepareFlip" in l or "SetFlipImmediate" in l:
        continue
    if "ProgressBar[0] =" in l and not (l.endswith("= 1%") or l.endswith("= 100%")):
        continue
    if l != prev:
        print(f"[{i:05d}] {l}")
        prev = l
        shown += 1
        if shown >= 180:
            print("... (truncado a 180 eventos unicos) ...")
            break
