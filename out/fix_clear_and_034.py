from pathlib import Path

# --- 1. En rsx_d3d12_backend.c: activar el bloqueo real en rsx_present_flip_already_rendered (sin has_clear) ---
d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
dtxt = d3d_path.read_text(encoding="latin-1")

dtxt = dtxt.replace(
    "if (clear_presents > 0 && s_d3d.has_clear) return 1;",
    "if (clear_presents > 0 && s_d3d.draw_count < 1500) return 1;"
)

# Y en d3d12_clear (linea 6071): presentar siempre el frame completo cuando llega el clear de color del frame nuevo
old_cgate = """        if (fc != 0) {
            if (fc == s_last_clear_boundary_flip)
                return;   /* no flip since last present -> not a real boundary */"""

new_cgate = """        if (0 && fc != 0) {
            if (fc == s_last_clear_boundary_flip)
                return;   /* no flip since last present -> not a real boundary */"""

if old_cgate in dtxt:
    dtxt = dtxt.replace(old_cgate, new_cgate, 1)
    print("[patch] d3d12_clear + rsx_present_flip_already_rendered: un solo Present por frame (cero robo de draws)!")

d3d_path.write_text(dtxt, encoding="latin-1")

# --- 2. En ppu_recomp_034.cpp: evitar pasar 0 - 8 (0xFFFFFFF8) en func_00AEEFE4 y func_00AEEC94 ---
p34 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_034.cpp")
t34 = p34.read_text(encoding="latin-1")

old_loop2 = """loc_00AEF170:
        ctx->gpr[9] = ppc_rldicl(ctx->gpr[9], 0, 32);
        ctx->gpr[10] = (int64_t)(int32_t)(0x37);
        ctx->gpr[9] = vm_read32(ctx->gpr[9] + 0x0);
        ctx->gpr[11] = ppc_rldicl(ctx->gpr[9], 0, 32);"""

new_loop2 = """loc_00AEF170:
        ctx->gpr[9] = ppc_rldicl(ctx->gpr[9], 0, 32);
        ctx->gpr[10] = (int64_t)(int32_t)(0x37);
        ctx->gpr[9] = vm_read32(ctx->gpr[9] + 0x0);
        if ((uint32_t)ctx->gpr[9] < 0x10000u) goto loc_00AEF1C0;
        ctx->gpr[11] = ppc_rldicl(ctx->gpr[9], 0, 32);"""

if old_loop2 in t34:
    t34 = t34.replace(old_loop2, new_loop2)
    print("[patch] func_00AEEFE4: protegido contra puntero nulo (0 - 8 = 0xFFFFFFF8)!")

old_c94 = "void func_00AEEC94(ppu_context* ctx) {"
new_c94 = "void func_00AEEC94(ppu_context* ctx) {\n        if ((uint32_t)ctx->gpr[4] >= 0xFFFFFF00u) return;"
if "if ((uint32_t)ctx->gpr[4] >= 0xFFFFFF00u) return;" not in t34 and old_c94 in t34:
    t34 = t34.replace(old_c94, new_c94, 1)
    print("[patch] func_00AEEC94: guarda contra 0xFFFFFFF8 agregada!")

p34.write_text(t34, encoding="latin-1")
