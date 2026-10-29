from pathlib import Path
import re

# --- 1. En spu_workload.c: liberar ls al terminar el hilo (sin importar sangria) ---
wl_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c")
wl_txt = wl_path.read_text(encoding="latin-1")
if "free(ls); free(j); return 0;" not in wl_txt:
    wl_txt, n = re.subn(r"free\(j\);\s*return 0;", "if (!ts_slot || ts_slot->ls != ls) free(ls); free(j); return 0;", wl_txt)
    wl_path.write_text(wl_txt, encoding="latin-1")
    print(f"[patch] spu_workload.c: liberacion de RAM free(ls) aplicada ({n} sitio(s))!")

# --- 2. En rsx_d3d12_backend.c: quitar bloqueo s_last_flip_present y unir UI + Fondo en d3d12_clear ---
d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

txt = txt.replace(
    "if (cur_fc != 0 && cur_fc == s_last_flip_present && s_d3d.draw_count < (MAX_DRAWS - 256))\n            return;",
    "(void)s_last_flip_present;"
)

old_clear = """        /* Color clear on display surface: record it in-place if we haven't flipped yet */
        if (s_d3d.clear_count < MAX_CLEARS) {
            ClearCmd* cc = &s_d3d.clears[s_d3d.clear_count++];
            cc->rt_off = 0; cc->before_draw = s_d3d.draw_count;
            cc->mask = mask;
            cc->r = r; cc->g = g; cc->b = b; cc->a = a;
        }
        return;"""

new_clear = """        int has_disp = 0;
        for (u32 _i = 0; _i < s_d3d.draw_count; _i++)
            if (s_d3d.draws[_i].rt_off == 0) { has_disp = 1; break; }
        if (!has_disp) {
            if (s_d3d.clear_count < MAX_CLEARS) {
                ClearCmd* cc = &s_d3d.clears[s_d3d.clear_count++];
                cc->rt_off = 0; cc->before_draw = s_d3d.draw_count;
                cc->mask = mask;
                cc->r = r; cc->g = g; cc->b = b; cc->a = a;
            }
            s_d3d.clear_r = r; s_d3d.clear_g = g;
            s_d3d.clear_b = b; s_d3d.clear_a = a;
            s_d3d.has_clear = 1;
            return;
        }
        if (s_d3d.initialized) {
            s_present_this_frame = 1;
            render_frame();
            s_clear_presents++;
            {
                extern unsigned cellGcm_flip_request_count(void);
                s_last_clear_presented_flip = cellGcm_flip_request_count();
            }
        }
        s_d3d.draw_count = 0;
        s_d3d.clear_count = 0;"""

if old_clear in txt:
    txt = txt.replace(old_clear, new_clear, 1)
    print("[patch] rsx_d3d12_backend.c: d3d12_clear actualizado (presenta en clear de Color 0xF0, une UI en clear de Depth 0x01)!")

d3d_path.write_text(txt, encoding="latin-1")

# --- 3. En spu_0021_at_018ECF00/spu_recomp.c (img=22): evitar spin en 208F8 cuando EAL (gpr[8]) == 0 ---
p21 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0021_at_018ECF00\spu_recomp.c")
t21 = p21.read_text(encoding="latin-1")
old_208f8 = "void spu_0021_at_018ECF00_spu_func_000208F8(spu_context* ctx) {\nloc_000208F8:"
new_208f8 = "void spu_0021_at_018ECF00_spu_func_000208F8(spu_context* ctx) {\n        if (ctx->gpr[8]._u32[0] < 0x10000u) { ctx->gpr[3] = spu_il(0); SPU_RET(ctx); }\nloc_000208F8:"
if "ctx->gpr[8]._u32[0] < 0x10000u" not in t21 and old_208f8 in t21:
    t21 = t21.replace(old_208f8, new_208f8, 1)
    p21.write_text(t21, encoding="latin-1")
    print("[patch] spu_0021 (img=22): eliminado spu-spin en 208F8 cuando ea == 0!")
