sp = open(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(sp):
    if "jc_run_one_job(" in l:
        print(f"=== 1. jc_run_one_job en cellSpurs.c:{i+1} ===")
        for j in range(i, min(len(sp), i+115)):
            print(f"{j+1:04d}: {sp[j]}")
        break

l29 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== 2. Escrituras a + 0x30 en ppu_recomp_029.cpp ===")
for i, l in enumerate(l29):
    if "+ 0x30," in l and "vm_write8" in l:
        print(f"Linea {i+1}: {l}")
        for j in range(max(0, i-12), min(len(l29), i+15)):
            print(f"  {j+1:06d}: {l29[j]}")
