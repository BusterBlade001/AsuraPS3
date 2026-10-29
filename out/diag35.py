path = r"C:\AsuraPS3\out\boot35.log"
lines = [l.strip() for l in open(path, "r", encoding="latin-1") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT35.LOG: {len(lines)} ===")

print("\n--- 1. ULTIMOS 45 EVENTOS AL CARGAR EL EPISODIO 1 ---")
ev = [f"[{i:05d}] {l}" for i, l in enumerate(lines) if any(k in l for k in ("[fs]", "[sys_fs]", "LFQPush", "spurs-job", "unresolved", "BLOCKED", "FAIL", "ERROR", "CRASH", "null-call", "queue pop", "spu-spin", "CreateTask"))]
for l in ev[-45:]:
    print(" ", l[:115])

print("\n--- 2. ULTIMAS 25 LINEAS DE BOOT35.LOG ---")
for l in lines[-25:]:
    print(" ", l[:115])
