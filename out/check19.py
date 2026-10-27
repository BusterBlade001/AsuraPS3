import os

if os.path.exists(r"C:\AsuraPS3\out\boot19.log"):
    lines = [l.strip() for l in open(r"C:\AsuraPS3\out\boot19.log", "r", encoding="latin-1") if l.strip()]
    print(f"=== TOTAL LINEAS EN BOOT19.LOG: {len(lines)} ===")
    for i, l in enumerate(lines):
        if any(k in l for k in ("spurs-job", ".BIK", "[FP]", "dumped ->", "HALT", "CRASH")):
            print(f"[{i:05d}] {l[:115]}")

if os.path.exists("fp_dump.hlsl"):
    print("\n=== SHADERS EN fp_dump.hlsl ===")
    for l in open("fp_dump.hlsl", "r", encoding="latin-1"):
        if "fp_addr=" in l or "return " in l:
            print(" ", l.strip()[:115])

d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(d3d):
    if "rsx_d3d12_backend_present(" in l:
        print(f"\n=== rsx_d3d12_backend_present en rsx_d3d12_backend.c:{i+1} ===")
        for j in range(max(0, i-20), min(len(d3d), i+110)):
            print(f"{j+1:04d}: {d3d[j]}")
        break
