from collections import Counter

path = r"C:\AsuraPS3\out\boot11.log"
lines = [l.strip() for l in open(path, "r", encoding="utf-8", errors="replace") if l.strip()]

print(f"=== TOTAL LINEAS EN BOOT11.LOG: {len(lines)} ===")

print("\n--- 1. ARCHIVOS ABIERTOS ([fs] open) DESPUES DE TROPHY ---")
fs_lines = [f"[{i:05d}] {l}" for i, l in enumerate(lines) if "[fs]" in l or "sceNpTrophy" in l]
for l in fs_lines[-40:]:
    print(l)

print("\n--- 2. CONTEO DE EVENTOS D3D12 / RSX / SPU / LFQ ---")
for key in ("draw_arrays", "draw_indexed", "[VP]", "[FP]", "LFQPush#", "EventFlagWait BLOCKED", "unresolved NID", "dispatch MISS", "chain 0x"):
    matches = [l for l in lines if key in l]
    print(f"  {key:22s}: {len(matches):6d} veces" + (f"  (ult: {matches[-1][:90]})" if matches else ""))

print("\n--- 3. REPORTE [gprof] Y [WATCHDOG] (15s y 28s) ---")
wd_lines = [f"[{i:05d}] {l}" for i, l in enumerate(lines) if "[WATCHDOG]" in l or "[gprof]" in l or "BLOCKED" in l]
for l in wd_lines[-70:]:
    print(l)
