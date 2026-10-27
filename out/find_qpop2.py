import glob

sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. cellSpurs.c (3060..3200) ===")
for j in range(3060, min(len(sp), 3200)):
    print(f"{j+1:04d}: {sp[j]}")

files = sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp"))
stub_fn = None
for p in files:
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "0x91066667" in txt.lower():
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "0x91066667" in l.lower():
                for k in range(i, max(-1, i-10), -1):
                    if lines[k].startswith("void func_"):
                        stub_fn = lines[k].split()[1].split("(")[0]
                        print(f"\nStub cellSpursQueuePopBody = {stub_fn}")
                        break

if stub_fn:
    for p in files:
        txt = open(p, "r", encoding="utf-8", errors="ignore").read()
        if stub_fn in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if stub_fn in l and not l.startswith(f"void {stub_fn}") and "function_table" not in l:
                    print(f"\n=== PPU CALLER OF {stub_fn} in {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(max(0, i-20), min(len(lines), i+20)):
                        print(f"{j+1:06d}: {lines[j]}")
