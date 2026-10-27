path = r"C:\AsuraPS3\out\boot.log"
raw = open(path, "rb").read().replace(b"\x00", b"").decode("utf-8", errors="replace")
lines = [l.strip() for l in raw.splitlines() if l.strip()]

skip_tokens = (
    "SetPrepareFlip", "SetFlipImmediate", "timer_usleep",
    "[fs] read", "[SEMA-REL]", "[LWM-BLOCK]", "[LWM-GOT]",
    "CLEAR_SURFACE", "[GET_REPORT]", "[usercmd]", "[RSX] label write"
)

prev = None
seen_100 = False
for i, l in enumerate(lines[280:], start=280):
    if any(t in l for t in skip_tokens):
        continue
    if "ProgressBar[0] =" in l:
        if "100%" in l and not seen_100:
            seen_100 = True
        else:
            continue
    if l != prev:
        print(f"[{i:05d}] {l}")
        prev = l
