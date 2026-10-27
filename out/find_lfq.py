import glob

# 1. Buscar quién llama al stub de 0x8A85674D (_cellSpursLFQueuePushBody) en PPU
files = sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp"))
stub_fn = None
for p in files:
    txt = open(p, "r", encoding="utf-8", errors="ignore").read()
    if "0x8a85674d" in txt.lower():
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "0x8a85674d" in l.lower():
                for k in range(i, max(-1, i-10), -1):
                    if lines[k].startswith("void func_"):
                        stub_fn = lines[k].split()[1].split("(")[0]
                        print(f"Stub _cellSpursLFQueuePushBody = {stub_fn}")
                        break

if stub_fn:
    for p in files:
        txt = open(p, "r", encoding="utf-8", errors="ignore").read()
        if stub_fn in txt:
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if stub_fn in l and not l.startswith(f"void {stub_fn}") and "function_table" not in l:
                    print(f"\n=== PPU CALLER OF {stub_fn} in {p.split('\\')[-1]}:{i+1} ===")
                    for j in range(max(0, i-25), min(len(lines), i+25)):
                        print(f"{j+1:06d}: {lines[j]}")

# 2. Ver cómo spu_workload.c maneja WAIT_SIGNAL y spu_taskset_signal_task
spu_wl = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(spu_wl):
    if "spu_taskset_signal_task" in l or "WAIT_SIGNAL" in l:
        print(f"\n=== spu_workload.c:{i+1} ===")
        for j in range(max(0, i-10), min(len(spu_wl), i+35)):
            print(f"{j+1:04d}: {spu_wl[j]}")
