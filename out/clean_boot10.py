path = r"C:\AsuraPS3\out\boot10.log"
lines = [l.strip() for l in open(path, "r", encoding="utf-8", errors="replace") if l.strip()]
print(f"=== Total lineas en boot10.log: {len(lines)} ===")

skip_tokens = (
    "SetPrepareFlip", "SetFlipImmediate", "timer_usleep",
    "[SEMA-REL]", "[LWM-BLOCK]", "[LWM-GOT]",
    "CLEAR_SURFACE", "[GET_REPORT]", "[usercmd]", "[RSX] label write",
    "port_send(port=7", "port_send(port=2", "queue_create -> id=7",
    "port_create -> id=7", "port_connect(port=7", "port_connect_local(port=7",
    "event_queue_receive(q=7", "event_queue_receive(q=2", "_SendSignal(taskset=0x01B79500",
    "WAIT_SIGNAL#", "signal task 0 (taskset 0x01B79500)"
)
filtered = []
prev = None
for i, l in enumerate(lines):
    if any(t in l for t in skip_tokens):
        continue
    if l != prev:
        filtered.append(f"[{i:05d}] {l}")
        prev = l

for l in filtered[-140:]:
    print(l)
