d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. rsx_d3d12_backend.c: vp_upload_tex_slot (2850..3035) ===")
for j in range(2850, 3035):
    print(f"{j+1:04d}: {d3d[j]}")

sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== 2. cellSpurs.c: EventFlagWait (2035..2095) ===")
for j in range(2035, 2095):
    print(f"{j+1:04d}: {sp[j]}")
