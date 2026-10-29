from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# Activar RSX_ACCUM_FRAME = 1 por defecto en d3d12_clear para no partir el frame en dos mitades (24 + 17 draws)
old_accum = 'if (accum < 0) { const char* e = getenv("RSX_ACCUM_FRAME"); accum = e ? atoi(e) : 0; }'
new_accum = 'if (accum < 0) { const char* e = getenv("RSX_ACCUM_FRAME"); accum = e ? atoi(e) : 1; }'

assert old_accum in txt, "old_accum not found"
txt = txt.replace(old_accum, new_accum, 1)
d3d_path.write_text(txt, encoding="latin-1")
print("[patch] RSX_ACCUM_FRAME=1 activado por defecto: los 41 draws ahora se presentan juntos sin parpadeo!")
