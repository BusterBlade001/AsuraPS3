p0 = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0000_at_017AA900\spu_recomp.c"
l0 = open(p0, "r", encoding="utf-8", errors="ignore").read().splitlines()

# Buscar spu_func_00015668 y funciones que usen 0x8041 (error codes de EventFlagSet)
for i, l in enumerate(l0):
    if "void spu_0000_at_017aa900_spu_func_00015668(" in l.lower():
        print(f"=== 1. spu_func_00015668 en spu_0000:{i+1} ===")
        for j in range(i, min(len(l0), i+110)):
            print(f"{j+1:05d}: {l0[j]}")
        break

for i, l in enumerate(l0):
    if "2313" in l or "0x909" in l.lower():
        print(f"\n=== Posible EventFlagSet en spu_0000:{i+1} ===")
        for j in range(max(0, i-30), min(len(l0), i+20)):
            print(f"{j+1:05d}: {l0[j]}")

sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== 2. cellSpurs.c (2500..2590) ===")
for j in range(2500, min(len(sp), 2590)):
    print(f"{j+1:04d}: {sp[j]}")
