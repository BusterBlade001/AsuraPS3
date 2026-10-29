from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# --- 1. En d3d12_clear: si (mask & 0xF0) == 0 (clear de solo Depth/Stencil a mitad de frame),
#        NO partir el frame ni borrar draw_count; solo encolar el clear de Depth/Stencil!
#        Y si es un clear de Color (mask & 0xF0), NUNCA llamar a render_frame() desde d3d12_clear
#        (solo reiniciar draw_count = 0 si el frame anterior ya fue presentado por FLIP). ---
old_clear_block = """    if (s_d3d.draw_count > 0) {
        int has_disp = 0;
        for (u32 _i = 0; _i < s_d3d.draw_count; _i++)
            if (s_d3d.draws[_i].rt_off == 0) { has_disp = 1; break; }
        if (!has_disp) {
            if (s_d3d.clear_Count < MAX_CLEARS) {
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
        { static int accum = -1;
          if (accum < 0) { const char* e = getenv("RSX_ACCUM_FRAME"); accum = e ? atoi(e) : 0; }
          if (accum) return; }
        if (s_d3d.initialized) {
            if (blink_dbg())
                printf("[CLEAR] presenting %u accumulated draws at frame boundary\\n",
                       s_d3d.draw_count);
            render_frame();
            s_clear_presents++;
            {
                extern unsigned cellGcm_flip_request_count(void);
                s_last_clear_presented_flip = cellGcm_flip_request_count();
            }
        }
        s_d3d.draw_count = 0;
        s_d3d.clear_count = 0;
    }"""

# Nota: en rsx_d3d12_backend.c es s_d3d.clear_count (minuscula)
old_clear_block = old_clear_block.replace("s_d3d.clear_Count", "s_d3d.clear_count")

new_clear_block = """    if (s_d3d.draw_count > 0) {
        /* If this is a Depth/Stencil-only clear ((mask & 0xF0) == 0) mid-frame before drawing UI,
         * record it in-place and NEVER split or wipe the color draws of the current frame! */
        if ((mask & 0xF0u) == 0) {
            if (s_d3d.clear_count < MAX_CLEARS) {
                ClearCmd* cc = &s_d3d.clears[s_d3d.clear_count++];
                cc->rt_off = 0; cc->before_draw = s_d3d.draw_count;
                cc->mask = mask;
                cc->r = r; cc->g = g; cc->b = b; cc->a = a;
            }
            return;
        }
        /* Color clear on display surface: record it in-place if we haven't flipped yet */
        if (s_d3d.clear_count < MAX_CLEARS) {
            ClearCmd* cc = &s_d3d.clears[s_d3d.clear_count++];
            cc->rt_off = 0; cc->before_draw = s_d3d.draw_count;
            cc->mask = mask;
            cc->r = r; cc->g = g; cc->b = b; cc->a = a;
        }
        return;
    }"""

assert old_clear_block in txt, "old_clear_block not found in rsx_d3d12_backend.c"
txt = txt.replace(old_clear_block, new_clear_block, 1)
d3d_path.write_text(txt, encoding="latin-1")
print("[patch] d3d12_clear corregido: los clears Depth/Stencil de mitad de frame ya no parten ni hacen parpadear la pantalla!")
