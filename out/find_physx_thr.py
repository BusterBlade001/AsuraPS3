import glob, json

# Buscar la funcion que apunta el OPD 0x01997000 o que contiene el bucle de PPU PhysX thread
for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    for needle in ["0x01997000", "PPU PhysX thread"]:
        if needle in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if needle in l:
                    print(f"=== Match {needle} in {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(max(0, i-20), min(len(lines), i+35)):
                        print(f"{j+1:06d}: {lines[j]}")

# Leer la direccion de codigo dentro del OPD 0x01997000 en el EBOOT.ELF
elf = open(r"C:\AsuraPS3\game\PS3_GAME\USRDIR\EBOOT.ELF", "rb").read()
# Buscar 0x01997000 en EBOOT.functions.json
funcs = json.load(open(r"C:\AsuraPS3\out\EBOOT.functions.json"))
flist = funcs["functions"] if isinstance(funcs, dict) and "functions" in funcs else funcs
for f in flist:
    if "01997000" in str(f):
        print("Func JSON:", f)
