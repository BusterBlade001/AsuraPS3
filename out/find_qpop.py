p0 = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0000_at_017AA900\spu_recomp.c"
l0 = open(p0, "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. spu_0000 (23940..24055) ===")
for j in range(23940, 24055):
    print(f"{j+1:05d}: {l0[j]}")

sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(sp):
    if "QueuePop" in l:
        print(f"\n=== 2. cellSpurs.c:{i+1} ===")
        for j in range(max(0, i-5), min(len(sp), i+55)):
            print(f"{j+1:04d}: {sp[j]}")
