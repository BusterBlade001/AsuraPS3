path = r"C:\AsuraPS3\out\boot33.log"
lines = [l.strip() for l in open(path, "r", encoding="latin-1") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT33.LOG: {len(lines)} ===")

print("\n--- 1. LINEAS [FP] EN BOOT33.LOG ---")
for l in lines:
    if "[FP]" in l:
        print(" ", l[:115])

print("\n--- 2. ARCHIVOS ABIERTOS DEL EPISODIO 1 (DESPUES DE fd 45) ---")
fs_ev = [f"[{i:05d}] {l}" for i, l in enumerate(lines) if any(k in l for k in ("[fs]", "[sys_fs]", "LFQPush", "spurs-job", "unresolved", "BLOCKED", "FAIL", "ERROR", "CRASH", "null-call"))]
for l in fs_ev[-55:]:
    print(" ", l[:115])

print("\n--- 3. ULTIMAS 25 LINEAS DEL LOG ---")
for l in lines[-25:]:
    print(" ", l[:115])
