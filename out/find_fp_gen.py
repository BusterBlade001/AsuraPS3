d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="latin-1").read().splitlines()

for i, l in enumerate(d3d):
    if "struct PSInput" in l or "static void render_frame(" in l:
        print(f"\n=== Match en rsx_d3d12_backend.c:{i+1} ===")
        for j in range(max(0, i-5), min(len(d3d), i+110)):
            print(f"{j+1:04d}: {d3d[j]}")
