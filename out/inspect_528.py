import glob

lines = [l.strip() for l in open(r"C:\AsuraPS3\out\boot18.log", "r", encoding="latin-1") if l.strip()]
print("=== 1. EVENTOS AL ENTRAR A TITLEMENU_BG00.BIK (47680..48300) ===")
skip = ("SetPrepareFlip", "SetFlipImmediate", "timer_usleep", "[SEMA-REL]", "[LWM-", "CLEAR_SURFACE",
        "[GET_REPORT]", "[usercmd]", "[RSX] label", "event_queue_receive(q=7")
prev = None
for i in range(47680, min(len(lines), 48300)):
    l = lines[i]
    if any(s in l for s in skip):
        continue
    if l != prev:
        print(f"[{i:05d}] {l[:120]}")
        prev = l

# 2. Buscar dónde está definido spu_run_spurs_job en runtime/spu/
for p in glob.glob(r"C:\AsuraPS3\ps3recomp\runtime\spu\*.c*"):
    txt = open(p, "r", encoding="latin-1").read()
    if "spu_run_spurs_job" in txt and "int rc = spu_run_spurs_job" not in txt:
        print(f"\n=== 2. spu_run_spurs_job en {p.split('\\')[-1]} ===")
        s_lines = txt.splitlines()
        for i, l in enumerate(s_lines):
            if "spu_run_spurs_job" in l:
                for j in range(max(0, i-5), min(len(s_lines), i+65)):
                    print(f"{j+1:04d}: {s_lines[j]}")
                break

# 3. Desensamblar spujob_D6E964B601AB14C0_528.bin (528 bytes = 132 instrucciones)
import sys
sys.path.insert(0, r"C:\AsuraPS3\ps3recomp\tools")
from spu_disasm import disasm_inst
raw = open(r"C:\AsuraPS3\out\jobmods\spujob_D6E964B601AB14C0_528.bin", "rb").read()
print(f"\n=== 3. DESENSAMBLADO DE spujob_D6E964B601AB14C0_528.bin ({len(raw)} bytes) ===")
for off in range(0, len(raw), 4):
    w = int.from_bytes(raw[off:off+4], "big")
    print(f"  0x{off:03X}: {w:08X}  {disasm_inst(w, off)}")
