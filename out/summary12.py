path = r"C:\AsuraPS3\out\boot12.log"
lines = [l.strip() for l in open(path, "r", encoding="utf-8", errors="replace") if l.strip()]
print(f"=== TOTAL LINEAS EN BOOT12.LOG: {len(lines)} ===")

print("\n--- 1. ARCHIVOS ABIERTOS ([fs] y [sys_fs]) ---")
fs_lines = [f"[{i:05d}] {l}" for i, l in enumerate(lines) if "[fs]" in l or "[sys_fs]" in l or "sceNpTrophy" in l]
for l in fs_lines[-45:]:
    print(l)

print("\n--- 2. CONTEO DE EVENTOS D3D12 / RSX / SPU / LFQ ---")
for key in ("draw_arrays", "draw_indexed", "[VP]", "[FP]", "LFQPush#", "EventFlagWait BLOCKED", "unresolved NID", "open FAILED"):
    matches = [l for l in lines if key in l]
    print(f"  {key:22s}: {len(matches):6d} veces" + (f"  (ult: {matches[-1][:90]})" if matches else ""))

print("\n--- 3. ESTADO DE HILOS EN [WATCHDOG] ---")
for i, l in enumerate(lines):
    if "[WATCHDOG]" in l and ("sample;" in l or "guest-tid" in l or "in " in l):
        print(f"[{i:05d}] {l}")
