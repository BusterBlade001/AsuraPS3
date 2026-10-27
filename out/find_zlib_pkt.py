p29 = r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp"
l29 = open(p29, "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. FUNCION PPU QUE ARMA EL PAQUETE DE 32 BYTES (65240..65385) ===")
for j in range(65240, 65385):
    print(f"{j+1:06d}: {l29[j]}")

pspu = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0001_at_017C1F00\spu_recomp.c"
lspu = open(pspu, "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== 2. MANEJADOR DEL PAQUETE EN SPU_0001 (370..620) ===")
for j in range(370, 620):
    print(f"{j+1:05d}: {lspu[j]}")
