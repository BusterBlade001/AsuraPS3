p = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spujob_42E1FC8CEE0BE246\spu_recomp.c"
lines = open(p, "r", encoding="latin-1").read().splitlines()

for i, l in enumerate(lines):
    if "spu_func_00000368(" in l and l.startswith("void "):
        print(f"=== 1. spu_func_00000368 (linea {i+1}) ===")
        for j in range(i, min(len(lines), i+110)):
            print(f"{j+1:05d}: {lines[j]}")
        break

print("\n=== 2. Todos los HALT-ASSERT en spujob_42E1FC8CEE0BE246 ===")
for i, l in enumerate(lines):
    if "HALT-ASSERT" in l:
        print(f"Linea {i+1}: {l}")
        for j in range(max(0, i-15), min(len(lines), i+8)):
            print(f"  {j+1:05d}: {lines[j]}")
