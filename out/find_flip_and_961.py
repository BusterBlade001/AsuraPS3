import glob

gcm = open(r"C:\AsuraPS3\ps3recomp\libs\video\cellGcmSys.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(gcm):
    if "cellGcmSetPrepareFlip(" in l or "cellGcmSetFlipImmediate(" in l:
        print(f"\n=== 1. cellGcmSys.c:{i+1} ===")
        for j in range(max(0, i-5), min(len(gcm), i+35)):
            print(f"{j+1:04d}: {gcm[j]}")

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    for fn in ["void func_00961CBC(", "void func_00961DA8("]:
        if fn in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if fn in l:
                    print(f"\n=== 2. {fn} en {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(i, min(len(lines), i+65)):
                        print(f"{j+1:06d}: {lines[j]}")
                    break
