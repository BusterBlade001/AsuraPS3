sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(sp):
    if "static int jc_execute(" in l:
        print(f"=== 1. jc_execute en cellSpurs.c:{i+1} ===")
        for j in range(i, min(len(sp), i+95)):
            print(f"{j+1:04d}: {sp[j]}")
        break

wl = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(wl):
    if "built SpursTasksetContext" in l:
        print(f"\n=== 2. spu_workload.c:{i+1} ===")
        for j in range(max(0, i-45), min(len(wl), i+55)):
            print(f"{j+1:04d}: {wl[j]}")
        break
