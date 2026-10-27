d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. rsx_d3d12_backend.c: QUADS (6070..6155) ===")
for j in range(6070, 6155):
    print(f"{j+1:04d}: {d3d[j]}")

print("\n=== 2. rsx_d3d12_backend.c: FP DECOMPILER (1980..2110) ===")
for j in range(1980, 2110):
    print(f"{j+1:04d}: {d3d[j]}")

sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(sp):
    if "CreateTask(id=" in l:
        print(f"\n=== 3. cellSpurs.c CreateTask ({i+1}) ===")
        for j in range(max(0, i-25), min(len(sp), i+40)):
            print(f"{j+1:04d}: {sp[j]}")
        break
