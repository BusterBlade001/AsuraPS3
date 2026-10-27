import glob

files = sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp"))

# 1. Ver las 80 líneas previas a loc_0089B384 en ppu_recomp_026.cpp
lines26 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_026.cpp", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== CONTEXTO PREVIO A loc_0089B384 (ppu_recomp_026.cpp) ===")
for j in range(122950, 123055):
    print(f"{j+1:06d}: {lines26[j]}")

# 2. Ver quién es func_016037C0 y todas las referencias a -0x1328 (0x019EECD8)
for path in files:
    txt = open(path, "r", encoding="utf-8", errors="ignore").read()
    if "void func_016037C0(" in txt or "-0x1328" in txt:
        lines = txt.splitlines()
        for i, line in enumerate(lines):
            if "void func_016037C0(" in line:
                print(f"\n=== func_016037C0 in {path.split('\\')[-1]}:{i+1} ===")
                for j in range(i, min(len(lines), i + 20)):
                    print(f"{j+1:06d}: {lines[j]}")
            if "-0x1328" in line:
                print(f"\n=== REF -0x1328 (0x019EECD8) in {path.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i - 15), min(len(lines), i + 20)):
                    print(f"{j+1:06d}: {lines[j]}")
