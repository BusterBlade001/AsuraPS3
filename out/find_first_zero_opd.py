lines = [l.strip() for l in open(r"C:\AsuraPS3\out\boot41.log", "r", encoding="latin-1") if l.strip()]
for i, l in enumerate(lines):
    if "code 0x00000000 not registered" in l:
        print(f"=== 1. Primera aparicion en linea {i} (contexto previo) ===")
        for j in range(max(0, i-35), min(len(lines), i+10)):
            print(f"[{j:05d}] {lines[j][:120]}")
        break

l28 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_028.cpp", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(l28):
    if "void func_00962088(" in l:
        print(f"\n=== 2. func_00962088 en ppu_recomp_028.cpp:{i+1} ===")
        for j in range(i, min(len(l28), i+75)):
            print(f"{j+1:06d}: {l28[j]}")
        break
