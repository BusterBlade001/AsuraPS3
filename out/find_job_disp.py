import glob

wl = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(wl):
    if "spu_workload_dispatch_job(" in l:
        print(f"=== 1. spu_workload_dispatch_job en spu_workload.c:{i+1} ===")
        for j in range(i, min(len(wl), i+95)):
            print(f"{j+1:04d}: {wl[j]}")
        break

for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "0098AADC" in txt or "0098A860" in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "loc_0098AADC:" in l or "loc_0098A860:" in l:
                print(f"\n=== 2. {l} en {p.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-15), min(len(lines), i+20)):
                    print(f"{j+1:06d}: {lines[j]}")
