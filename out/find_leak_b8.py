import glob

# 1. Ver func_00A7901C (CellMemoryManager)
for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "void func_00A7901C(" in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "void func_00A7901C(" in l:
                print(f"=== 1. func_00A7901C en {p.split('\\')[-1]}:{i+1} ===")
                for j in range(i, min(len(lines), i+90)):
                    print(f"{j+1:06d}: {lines[j]}")
                break

# 2. Ver dónde cellSpurs.c envía eventos al terminar un JobChain (END after)
sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(sp):
    if "END after" in l:
        print(f"\n=== 2. cellSpurs.c:{i+1} ===")
        for j in range(max(0, i-45), min(len(sp), i+25)):
            print(f"{j+1:04d}: {sp[j]}")

# 3. Ver dónde rsx_d3d12_backend.c sube las texturas 0x81 (B8) a D3D12
d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(d3d):
    if "0x81" in l and i < 6400:
        print(f"\n=== 3. rsx_d3d12_backend.c:{i+1} ===")
        for j in range(max(0, i-15), min(len(d3d), i+35)):
            print(f"{j+1:04d}: {d3d[j]}")
