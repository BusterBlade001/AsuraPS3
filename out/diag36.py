path = r"C:\AsuraPS3\out\boot36.log"
lines = [l.strip() for l in open(path, "r", encoding="latin-1") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT36.LOG: {len(lines)} ===")

ev = [f"[{i:05d}] {l}" for i, l in enumerate(lines) if any(k in l for k in ("[fs]", "[sys_fs]", "[FP]", "allocate(", "LFQPush", "offscreen RT", "FAIL", "ERROR", "CRASH"))]
for l in ev[-40:]:
    print(" ", l[:115])

print("\n--- ULTIMAS 20 LINEAS ---")
for l in lines[-20:]:
    print(" ", l[:115])
