sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(sp):
    if "ShutdownTaskset(" in l or "JoinTaskset(" in l:
        print(f"=== cellSpurs.c:{i+1} ===")
        for j in range(max(0, i-5), min(len(sp), i+30)):
            print(f"{j+1:04d}: {sp[j]}")

p0 = open(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0000_at_017AA900\spu_recomp.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(p0):
    if "void spu_0000_at_017aa900_spu_func_000078f8(" in l.lower():
        print(f"\n=== spu_func_000078F8 en spu_0000:{i+1} ===")
        for j in range(i, min(len(p0), i+95)):
            print(f"{j+1:05d}: {p0[j]}")
        break
