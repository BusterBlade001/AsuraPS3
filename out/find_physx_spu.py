import glob

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    for fn in ["void func_00A30BDC(", "void func_00A30914("]:
        if fn in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if fn in l:
                    print(f"=== 1. {fn} en {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(i, min(len(lines), i+75)):
                        print(f"{j+1:06d}: {lines[j]}")
                    break

p21 = open(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0021_at_018ECF00\spu_recomp.c", "r", encoding="latin-1").read().splitlines()
print("\n=== 2. Entrada de spu_0021 (img=22, primeras 100 lineas) ===")
for j in range(0, min(100, len(p21))):
    print(f"{j+1:05d}: {p21[j]}")
