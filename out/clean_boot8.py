path = r"C:\AsuraPS3\out\boot8.log"
lines = [l.strip() for l in open(path, "r", encoding="utf-8", errors="replace") if l.strip()]
print(f"=== Total lineas en boot8.log: {len(lines)} ===")

skip_tokens = (
    "SetPrepareFlip", "SetFlipImmediate", "timer_usleep",
    "[SEMA-REL]", "[LWM-BLOCK]", "[LWM-GOT]",
    "CLEAR_SURFACE", "[GET_REPORT]", "[usercmd]", "[RSX] label write"
)
prev = None
for i, l in enumerate(lines):
    if any(t in l for t in skip_tokens):
        continue
    if l != prev:
        print(f"[{i:05d}] {l}")
        prev = l
