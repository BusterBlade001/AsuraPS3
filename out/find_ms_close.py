import glob

l29 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp", "r", encoding="utf-8", errors="ignore").read().splitlines()
fn_name = None
for j in range(45055, 45000, -1):
    if l29[j].startswith("void func_"):
        fn_name = l29[j].split()[1].split("(")[0]
        print(f"=== FUNCION DE CIERRE MULTISTREAM: {fn_name} (linea {j+1}) ===")
        for k in range(j, 45060):
            print(f"{k+1:06d}: {l29[k]}")
        break

if fn_name:
    for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
        txt = open(p, "r", encoding="utf-8", errors="ignore").read()
        if fn_name not in txt:
            continue
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if fn_name in l and not l.startswith(f"void {fn_name}") and "function_table" not in l:
                print(f"\n=== CALLER OF {fn_name} in {p.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-35), min(len(lines), i+20)):
                    print(f"{j+1:06d}: {lines[j]}")
