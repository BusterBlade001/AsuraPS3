d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="latin-1").read().splitlines()
print("=== 1. render_frame en rsx_d3d12_backend.c (6520..6750) ===")
for j in range(6520, min(len(d3d), 6750)):
    print(f"{j+1:04d}: {d3d[j]}")

for i, l in enumerate(d3d):
    if "PSO FAIL" in l:
        print(f"\n=== 2. PSO FAIL en rsx_d3d12_backend.c:{i+1} ===")
        for j in range(max(0, i-40), min(len(d3d), i+20)):
            print(f"{j+1:04d}: {d3d[j]}")
        break
