# 1. Ver dónde spu_0000 (image=1) salta desde 0x03930 y dónde señala el EventFlag
p0 = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0000_at_017AA900\spu_recomp.c"
l0 = open(p0, "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. SPU_0000 ALREDEDOR DE 0x03930 (primeras 260 lineas) ===")
for j in range(0, min(260, len(l0))):
    print(f"{j+1:05d}: {l0[j]}")

# 2. Ver cómo cellGcmSys.c maneja FIFO resync (jump-park)
gcm = open(r"C:\AsuraPS3\ps3recomp\libs\video\cellGcmSys.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(gcm):
    if "jump-park" in l:
        print(f"\n=== 2. cellGcmSys.c:{i+1} ===")
        for j in range(max(0, i-35), min(len(gcm), i+25)):
            print(f"{j+1:04d}: {gcm[j]}")
