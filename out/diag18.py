path = r"C:\AsuraPS3\out\boot18.log"
lines = [l.strip() for l in open(path, "r", encoding="latin-1") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT18.LOG: {len(lines)} ===")

print("\n--- 1. ARCHIVOS ABIERTOS Y VIDEOS .BIK ---")
for i, l in enumerate(lines):
    if any(k in l for k in (".BIK", "[fs] open", "[sys_fs]", "dumped ->", "ERROR", "CRASH", "BLOCKED")):
        print(f"[{i:05d}] {l[:115]}")

print("\n--- 2. HILOS EN [WATCHDOG] ---")
for i, l in enumerate(lines):
    if "[WATCHDOG]" in l and ("sample;" in l or "guest-tid" in l or "in " in l):
        print(f"[{i:05d}] {l}")

print("\n--- 3. ULTIMAS 25 LINEAS DE BOOT18.LOG ---")
for l in lines[-25:]:
    print(" ", l[:115])

wl = open(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c", "r", encoding="latin-1").read().splitlines()
for i, l in enumerate(wl):
    if "spu_run_spurs_job(" in l and i < 880:
        print(f"\n--- 4. spu_run_spurs_job en spu_workload.c:{i+1} ---")
        for j in range(i, min(len(wl), i+65)):
            print(f"{j+1:04d}: {wl[j]}")
        break
