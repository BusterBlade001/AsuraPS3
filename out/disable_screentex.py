from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

old_en = 'if (en < 0) { const char* e = getenv("SCREEN_AS_TEX"); en = e ? atoi(e) : 1; }'
new_en = 'if (en < 0) { const char* e = getenv("SCREEN_AS_TEX"); en = e ? atoi(e) : 0; }'

assert old_en in txt, "No se encontro SCREEN_AS_TEX en rsx_d3d12_backend.c"
txt = txt.replace(old_en, new_en, 1)
d3d_path.write_text(txt, encoding="latin-1")
print("[patch] SCREEN_AS_TEX puesto en 0 por defecto en rsx_d3d12_backend.c!")
