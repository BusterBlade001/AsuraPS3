import glob

# 1. Ver el inicio de func_0089B1D8 (lineas 122860 a 123045 de ppu_recomp_026.cpp)
lines26 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_026.cpp", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== INICIO DE func_0089B1D8 ===")
for j in range(122860, 123045):
    print(f"{j+1:06d}: {lines26[j]}")

# 2. Buscar todos los lugares que llaman a func_0089B1D8 SIN comprobar -0x1328 justo antes
print("\n=== LLAMADORES DIRECTOS A func_0089B1D8 ===")
for path in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(path, "r", encoding="utf-8", errors="ignore").read()
    if "func_0089B1D8" not in txt:
        continue
    lines = txt.splitlines()
    for i, line in enumerate(lines):
        if "func_0089B1D8" in line and "void func_0089B1D8" not in line:
            ctx_window = "\n".join(lines[max(0, i-8):i+1])
            if "-0x1328" not in ctx_window:
                print(f"\n--- Caller in {path.split('\\')[-1]}:{i+1} ---")
                for j in range(max(0, i-15), min(len(lines), i+6)):
                    print(f"{j+1:06d}: {lines[j]}")
