sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="latin-1").read().splitlines()
print("=== 1. cellSpurs.c (2740..2875) ===")
for j in range(2740, min(len(sp), 2875)):
    print(f"{j+1:04d}: {sp[j]}")

b27 = [l.strip() for l in open(r"C:\AsuraPS3\out\boot27.log", "r", encoding="latin-1") if l.strip()]
print(f"\n=== 2. Ultimas 35 lineas de boot27.log (total {len(b27)}) ===")
for l in b27[-35:]:
    print(" ", l[:115])
