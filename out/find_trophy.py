import glob

files = sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp"))
stub_fn = None
for p in files:
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "0x49d18217" in txt.lower():
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "0x49d18217" in l.lower():
                for k in range(i, max(-1, i-10), -1):
                    if lines[k].startswith("void func_"):
                        stub_fn = lines[k].split()[1].split("(")[0]
                        print(f"Stub sceNpTrophyGetGameInfo = {stub_fn}")
                        break

if stub_fn:
    for p in files:
        txt = open(p, "r", encoding="utf-8", errors="ignore").read()
        if stub_fn in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if stub_fn in l and not l.startswith(f"void {stub_fn}") and "function_table" not in l:
                    print(f"\n=== HILO TrophyInfo ({p.split('\\')[-1]}:{i+1}) ===")
                    for j in range(max(0, i-45), min(len(lines), i+65)):
                        print(f"{j+1:06d}: {lines[j]}")

for p in glob.glob(r"C:\AsuraPS3\ps3recomp\libs\**\sceNpTrophy.c", recursive=True):
    print(f"\n=== {p} ===")
    print(open(p, "r", encoding="utf-8", errors="ignore").read())
