import glob

for p in glob.glob(r"C:\AsuraPS3\ps3recomp\runtime\spu\*.c*") + glob.glob(r"C:\AsuraPS3\ps3recomp\libs\**\*.c*"):
    txt = open(p, "r", encoding="latin-1").read()
    for needle in ["[mfc-list] STALL", "REAL SpursTasksetContext"]:
        if needle in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if needle in l:
                    print(f"\n=== {needle} en {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(max(0, i-25), min(len(lines), i+30)):
                        print(f"{j+1:04d}: {lines[j]}")
                    break

p21 = open(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0021_at_018ECF00\spu_recomp.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(p21):
    if "void spu_0021_at_018ecf00_spu_func_000208a0(" in l.lower():
        print(f"\n=== spu_func_000208A0 en spu_0021:{i+1} ===")
        for j in range(i, min(len(p21), i+40)):
            print(f"{j+1:05d}: {p21[j]}")
        break
