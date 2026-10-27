from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")
lines = txt.splitlines()

print("=== Lineas 4850..4925 de rsx_d3d12_backend.c ===")
for j in range(4850, min(len(lines), 4925)):
    print(f"{j+1:04d}: {lines[j]}")

# Buscar la condicion de screen_copy_valid antes de 'bound frame copy at unit' y apagarla
for i, l in enumerate(lines):
    if "bound frame copy at unit" in l:
        for k in range(i, max(0, i-20), -1):
            if "screen_copy_valid" in lines[k]:
                lines[k] = "                if (0) {"
                print(f"\n[patch] Desactivado secuestro screen_copy en linea {k+1}!")
                break

d3d_path.write_text("\n".join(lines) + "\n", encoding="latin-1")
