path = r"C:\AsuraPS3\out\boot37.log"
lines = [l.strip() for l in open(path, "r", encoding="latin-1") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT37.LOG: {len(lines)} ===")

print("\n--- 1. LINEAS [PERF] Y MEMORIA EN BOOT37.LOG ---")
for l in [x for x in lines if "[PERF]" in x or "allocate(" in x][-25:]:
    print(" ", l[:115])

print("\n--- 2. ULTIMOS 30 EVENTOS ---")
ev = [f"[{i:05d}] {l}" for i, l in enumerate(lines) if any(k in l for k in ("[fs]", "[sys_fs]", "[FP]", "LFQPush", "FAIL", "ERROR", "CRASH", "spu-spin", "STALL", "join("))]
for l in ev[-30:]:
    print(" ", l[:115])

wl = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c", "r", encoding="latin-1").read().splitlines()
print("\n--- 3. Final de spu_thread_entry en spu_workload.c (840..900) ---")
for j in range(840, min(len(wl), 900)):
    print(f"{j+1:04d}: {wl[j]}")
