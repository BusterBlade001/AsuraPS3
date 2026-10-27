l26 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_026.cpp", "r", encoding="utf-8", errors="ignore").read().splitlines()
for i, l in enumerate(l26):
    if "+ 0x354)" in l:
        window = "\n".join(l26[max(0, i-15):min(len(l26), i+15)])
        if "+ 0x350)" in window:
            print(f"\n=== Match in ppu_recomp_026.cpp:{i+1} ===")
            for j in range(max(0, i-45), min(len(l26), i+45)):
                print(f"{j+1:06d}: {l26[j]}")

l29 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== ppu_recomp_029.cpp (64020..64160) ===")
for j in range(64020, 64160):
    print(f"{j+1:06d}: {l29[j]}")
