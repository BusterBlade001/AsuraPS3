pspu = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0001_at_017C1F00\spu_recomp.c"
lspu = open(pspu, "r", encoding="utf-8", errors="ignore").read().splitlines()

for name in ["spu_func_0000af20(", "spu_func_0000afe0(", "spu_func_00003d80("]:
    for i, l in enumerate(lspu):
        if name in l.lower() and l.startswith("void "):
            print(f"\n=== {name} (linea {i+1}) ===")
            for j in range(i, min(len(lspu), i + 55)):
                print(f"{j+1:05d}: {lspu[j]}")
            break

p29 = r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp"
l29 = open(p29, "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== RESTO DE func_00999C4C Y SIGUIENTE FUNCION EN ppu_recomp_029.cpp (65380..65500) ===")
for j in range(65380, min(len(l29), 65500)):
    print(f"{j+1:06d}: {l29[j]}")
