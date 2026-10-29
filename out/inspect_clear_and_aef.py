p34 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_034.cpp", "r", encoding="latin-1").read().splitlines()
print("=== 1. Resto de func_00AEEFE4 (33465..33545) ===")
for j in range(33465, min(len(p34), 33545)):
    print(f"{j+1:06d}: {p34[j]}")

d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(d3d):
    if "static void d3d12_clear(" in l:
        print(f"\n=== 2. d3d12_clear actual (linea {i+1}) ===")
        for j in range(i, min(len(d3d), i+70)):
            print(f"{j+1:04d}: {d3d[j]}")
        break

for i, l in enumerate(d3d):
    if "void rsx_d3d12_backend_present(" in l:
        print(f"\n=== 3. rsx_d3d12_backend_present actual (linea {i+1}) ===")
        for j in range(i, min(len(d3d), i+55)):
            print(f"{j+1:04d}: {d3d[j]}")
        break
