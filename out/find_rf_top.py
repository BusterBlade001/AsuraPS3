d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="latin-1").read().splitlines()
print("=== 1. Inicio de render_frame (6300..6520) ===")
for j in range(6300, 6520):
    print(f"{j+1:04d}: {d3d[j]}")

import os
if os.path.exists("fp_dump.hlsl"):
    hlsl = open("fp_dump.hlsl", "r", encoding="latin-1").read()
    idx = hlsl.find("fp_addr=0x00001441")
    if idx != -1:
        print("\n=== 2. Shader fp_addr=0x00001441 en fp_dump.hlsl ===")
        print(hlsl[idx:idx+1800])
