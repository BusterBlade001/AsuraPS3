lines = [l.strip() for l in open(r"C:\AsuraPS3\out\boot41.log", "r", encoding="latin-1") if l.strip()]
print("=== 1. Lineas 51480..51555 de boot41.log ===")
for i in range(51480, min(len(lines), 51555)):
    print(f"[{i:05d}] {lines[i][:120]}")

m = open(r"C:\AsuraPS3\ps3recomp\templates\project\main.cpp", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(m):
    if "frame_clock(" in l or "rsx_present_frame(" in l:
        print(f"\n=== 2. main.cpp:{i+1} ===")
        for j in range(max(0, i-5), min(len(m), i+45)):
            print(f"{j+1:04d}: {m[j]}")
