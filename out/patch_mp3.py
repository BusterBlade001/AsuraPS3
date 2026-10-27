from pathlib import Path

p29 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp")
t29 = p29.read_text(encoding="utf-8")

old_mp3 = "void func_009935D4(ppu_context* ctx) {"
new_mp3 = "void func_009935D4(ppu_context* ctx) {\n\tctx->gpr[3] = 0;\n\treturn;"

assert old_mp3 in t29, "func_009935D4 not found in ppu_recomp_029.cpp"
if "void func_009935D4(ppu_context* ctx) {\n\tctx->gpr[3] = 0;" not in t29:
    t29 = t29.replace(old_mp3, new_mp3, 1)
    p29.write_text(t29, encoding="utf-8")
    print("[patch] func_009935D4 (cellMSMP3Init) ahora devuelve CELL_OK (0)!")
