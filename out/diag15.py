path = r"C:\AsuraPS3\out\boot15.log"
lines = [l.strip() for l in open(path, "r", encoding="utf-8", errors="replace") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT15.LOG: {len(lines)} ===")

for i, l in enumerate(lines):
    if any(k in l for k in ("[TEXFMT]", ".BIK", "[FP]", "CreateTask(", "ERROR", "CRASH")):
        print(f"[{i:05d}] {l[:115]}")

import os
if os.path.exists("fp_dump.hlsl"):
    print("\n=== SHADERS EN fp_dump.hlsl ===")
    hlsl = open("fp_dump.hlsl", "r", encoding="utf-8", errors="replace").read().splitlines()
    for l in hlsl[:140]:
        print(l)
