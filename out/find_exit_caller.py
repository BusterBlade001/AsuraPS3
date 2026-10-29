import glob

lines = [l.strip() for l in open(r"C:\AsuraPS3\out\boot41.log", "r", encoding="latin-1") if l.strip()]
print("=== 1. Lineas 52200..52405 de boot41.log ===")
for i in range(52200, min(len(lines), 52405)):
    print(f"[{i:05d}] {lines[i][:120]}")

print("\n=== 2. Llamadores de func_00961CBC y func_00961DA8 ===")
for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    for fn in ["func_00961CBC", "func_00961DA8"]:
        if fn in txt:
            pl = txt.splitlines()
            for i, l in enumerate(pl):
                if fn in l and not l.startswith("void ") and "function_table" not in l:
                    print(f"\n--- {fn} llamado en {p.split('\\')[-1]}:{i+1} ---")
                    for j in range(max(0, i-25), min(len(pl), i+15)):
                        print(f"{j+1:06d}: {pl[j]}")
