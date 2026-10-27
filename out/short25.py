d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(d3d):
    if "bound frame copy at unit" in l:
        print(f"=== 1. Bloque [SCREENTEX] en rsx_d3d12_backend.c:{i+1} ===")
        for j in range(max(0, i-25), min(len(d3d), i+15)):
            print(f"{j+1:04d}: {d3d[j]}")
        break

b25 = open(r"C:\AsuraPS3\out\boot25.log", "r", encoding="latin-1").read().splitlines()
print(f"\n=== 2. Eventos spurs-job / HALT / FP / BIK en boot25.log (total {len(b25)} lineas) ===")
shown = 0
for i, l in enumerate(b25):
    if any(k in l for k in ("spurs-job", "HALT", "[FP]", ".BIK", "CRASH", "ERROR", "offscreen RT")):
        print(f"[{i:05d}] {l[:115]}")
        shown += 1
        if shown >= 55:
            break

p_job = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spujob_D6E964B601AB14C0\spu_recomp.c"
j_lines = open(p_job, "r", encoding="latin-1").read().splitlines()
print(f"\n=== 3. spujob_D6E964B601AB14C0/spu_recomp.c ({len(j_lines)} lineas) ===")
for j in range(0, min(len(j_lines), 90)):
    print(f"{j+1:04d}: {j_lines[j]}")
