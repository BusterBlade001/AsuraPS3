path = r"C:\AsuraPS3\out\boot11.log"
lines = [l.strip() for l in open(path, "r", encoding="utf-8", errors="replace") if l.strip()]

print("=== 1. EVENTOS DESPUES DE [11139] GetGameInfo ===")
skip = ("SetPrepareFlip", "SetFlipImmediate", "timer_usleep", "[SEMA-REL]", "[LWM-", "CLEAR_SURFACE",
        "[GET_REPORT]", "[usercmd]", "[RSX] label", "port_send", "queue_create", "port_create",
        "port_connect", "event_queue_receive", "_SendSignal", "WAIT_SIGNAL", "signal task", "[gprof]", "[WATCHDOG]")
prev = None
shown = 0
for i, l in enumerate(lines[11138:], start=11138):
    if any(s in l for s in skip):
        continue
    if l != prev:
        print(f"[{i:05d}] {l}")
        prev = l
        shown += 1
        if shown >= 50:
            break

print("\n=== 2. LINEAS DE [WATCHDOG] ===")
for i, l in enumerate(lines):
    if "[WATCHDOG]" in l:
        print(f"[{i:05d}] {l}")
