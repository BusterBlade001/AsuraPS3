from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")
lines = txt.splitlines()

for i, l in enumerate(lines):
    if "[SCREENTEX]" in l:
        print(f"=== Contexto de [SCREENTEX] en rsx_d3d12_backend.c:{i+1} ===")
        for j in range(max(0, i-35), min(len(lines), i+20)):
            print(f"{j+1:04d}: {lines[j]}")
        break

# Desactivar screen_copy_valid para que [SCREENTEX] jamas reemplace el plano Y (1280x720) de Bink Video
old_sc = "s_d3d.screen_copy_valid = 1;"
new_sc = "s_d3d.screen_copy_valid = 0; /* disabled: hijacks Bink 1280x720 Y plane */"
if old_sc in txt:
    txt = txt.replace(old_sc, new_sc)
    d3d_path.write_text(txt, encoding="latin-1")
    print("\n[patch] [SCREENTEX] desactivado! Ahora unit=0 sube el plano Y real de 1280x720 de Bink Video!")
