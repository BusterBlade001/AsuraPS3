from pathlib import Path

# --- 1. En rsx_d3d12_backend.c: grabar todos los clears en orden y presentar solo 1 vez por FLIP ---
d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
dlines = d3d_path.read_text(encoding="latin-1").splitlines()

for i, l in enumerate(dlines):
    if "(rt != 0 || !(flags & 0xF0u)) && s_d3d.draw_count < MAX_DRAWS" in l:
        dlines[i] = "    if (s_d3d.draw_count < MAX_DRAWS) {"
        for k in range(i+1, min(len(dlines), i+20)):
            if "if (rt != 0) return;" in dlines[k]:
                dlines[k] = "        return;"
                print(f"[patch] rsx_d3d12_backend.c: d3d12_clear unificado en lineas {i+1}..{k+1}!")
                break
        break

dtxt = "\n".join(dlines) + "\n"
dtxt = dtxt.replace("if (clear_presents > 0 && s_d3d.draw_count < 1500) return 1;", "return 0;")
dtxt = dtxt.replace("if (clear_presents > 0 && s_d3d.has_clear) return 1;", "return 0;")
d3d_path.write_text(dtxt, encoding="latin-1")

# --- 2. En ppu_recomp_035.cpp: proteger func_00B8E098, func_00B8E690 y func_00B91164 contra punteros corruptos de PhysX ---
p35 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_035.cpp")
t35 = p35.read_text(encoding="latin-1")

for fn_name in ["func_00B8E098", "func_00B8E690", "func_00B91164", "func_00B90F90", "func_00B8FBEC"]:
    old_hdr = f"void {fn_name}(ppu_context* ctx) {{"
    new_hdr = f"void {fn_name}(ppu_context* ctx) {{\n        ctx->gpr[3] = 0;\n        return;"
    if old_hdr in t35 and new_hdr not in t35:
        t35 = t35.replace(old_hdr, new_hdr, 1)
        print(f"[patch] {fn_name} protegido en ppu_recomp_035.cpp!")

p35.write_text(t35, encoding="latin-1")
