p = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0001_at_017C1F00\spu_recomp.c"
lines = open(p, "r", encoding="utf-8", errors="ignore").read().splitlines()

print("=== 1. FIN DEL BUCLE ZLIB EN SPU_0001 (lineas 250..370) ===")
for j in range(250, min(370, len(lines))):
    print(f"{j+1:05d}: {lines[j]}")

for i, l in enumerate(lines):
    if "spu_func_0000a238(" in l.lower() and l.startswith("void "):
        print(f"\n=== 2. spu_func_0000A238 (linea {i+1}) ===")
        for j in range(i, min(len(lines), i + 140)):
            print(f"{j+1:05d}: {lines[j]}")
        break

spurs = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(spurs):
    if "cellSpursEventFlagInitialize(" in l or "cellSpursEventFlagWait(" in l:
        print(f"\n=== 3. cellSpurs.c:{i+1} ===")
        for j in range(max(0, i-5), min(len(spurs), i + 65)):
            print(f"{j+1:04d}: {spurs[j]}")
