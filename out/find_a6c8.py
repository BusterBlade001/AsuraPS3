p = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0001_at_017C1F00\spu_recomp.c"
lines = open(p, "r", encoding="utf-8", errors="ignore").read().splitlines()

print("=== 1. BUCLE PRINCIPAL DE ZLIB (lineas 140..250) ===")
for j in range(140, min(250, len(lines))):
    print(f"{j+1:05d}: {lines[j]}")

print("\n=== 2. LFQueuePopBegin (lineas 8910..9060) ===")
for j in range(8910, min(9060, len(lines))):
    print(f"{j+1:05d}: {lines[j]}")

for i, l in enumerate(lines):
    if "spu_func_0000a6c8(" in l.lower() and l.startswith("void "):
        print(f"\n=== 3. spu_func_0000A6C8 (linea {i+1}) ===")
        for j in range(i, min(len(lines), i + 120)):
            print(f"{j+1:05d}: {lines[j]}")
        break
