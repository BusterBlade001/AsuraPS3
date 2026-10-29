import glob

l27 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_027.cpp", "r", encoding="latin-1").read().splitlines()
print("=== 1. func_008A8CCC en ppu_recomp_027.cpp (1760..1810) ===")
for j in range(1760, 1810):
    print(f"{j+1:06d}: {l27[j]}")

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    for fn in ["void func_014315E8(", "void func_0090C930(", "void func_0004071C("]:
        if fn in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if fn in l:
                    print(f"\n=== 2. {fn} en {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(i, min(len(lines), i+65)):
                        print(f"{j+1:06d}: {lines[j]}")
                    break
