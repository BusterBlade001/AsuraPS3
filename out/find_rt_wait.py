import glob

l26 = open(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_026.cpp", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("=== 1. Funcion en 0x00889120 (ppu_recomp_026.cpp:82675..82740) ===")
for j in range(82675, 82740):
    print(f"{j+1:06d}: {l26[j]}")

# Buscar nombre de esa funcion y quién la llama, además de func_008985E4
fn_889 = None
for j in range(82715, 82600, -1):
    if l26[j].startswith("void func_"):
        fn_889 = l26[j].split()[1].split("(")[0]
        print("Nombre de la funcion en 82719:", fn_889)
        break

for i, l in enumerate(l26):
    if "void func_008985E4(" in l:
        print(f"\n=== 2. func_008985E4 en ppu_recomp_026.cpp:{i+1} ===")
        for k in range(i, min(len(l26), i+600)):
            if fn_889 and fn_889 in l26[k]:
                for m in range(max(i, k-35), min(len(l26), k+25)):
                    print(f"{m+1:06d}: {l26[m]}")
                break
        break

sfs = open(r"C:\AsuraPS3\ps3recomp\runtime\syscalls\sys_fs.c", "r", encoding="utf-8", errors="ignore").read().splitlines()
print("\n=== 3. runtime/syscalls/sys_fs.c (120..210) ===")
for j in range(120, min(len(sfs), 210)):
    print(f"{j+1:04d}: {sfs[j]}")
