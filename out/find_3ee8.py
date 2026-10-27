p = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spujob_42E1FC8CEE0BE246\spu_recomp.c"
lines = open(p, "r", encoding="latin-1").read().splitlines()

print("=== 1. Entrada de spujob_42E1FC8CEE0BE246 (primeras 90 lineas) ===")
for j in range(0, min(90, len(lines))):
    print(f"{j+1:05d}: {lines[j]}")

for i, l in enumerate(lines):
    if "03ee8" in l.lower() or "3ee8" in l.lower():
        print(f"\n=== 2. HALT-ASSERT en 0x03EE8 (linea {i+1}) ===")
        for j in range(max(0, i-45), min(len(lines), i+35)):
            print(f"{j+1:05d}: {lines[j]}")
        break
