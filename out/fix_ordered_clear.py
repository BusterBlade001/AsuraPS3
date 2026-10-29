from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# 1. En d3d12_clear: grabar TODOS los clears (incluyendo color en rt == 0) en orden dentro de s_d3d.draws[]
#    y retornar sin llamar a render_frame() desde d3d12_clear (para que solo el FLIP real de main.cpp presente el frame)
old_c21 = """    if ((rt != 0 || !(flags & 0xF0u)) && s_d3d.draw_count < MAX_DRAWS) {
        DrawRecord* dr = &s_d3d.draws[s_d3d.draw_count++];
        memset(dr, 0, sizeof(*dr));
        dr->is_clear    = 1;
        dr->rt_off      = rt;
        dr->rt_fmt      = st->surface_format;
        dr->rt_clip_w   = st->surface_clip_w;
        dr->rt_clip_h   = st->surface_clip_h;
        dr->clear_flags = flags;
        dr->clear_r = r; dr->clear_g = g; dr->clear_b = b; dr->clear_a = a;
        dr->clear_z = st->clear_z;
        dr->clear_s = st->clear_s;
        if (rt != 0) return;
    }"""

new_c21 = """    if (s_d3d.draw_count < MAX_DRAWS) {
        DrawRecord* dr = &s_d3d.draws[s_d3d.draw_count++];
        memset(dr, 0, sizeof(*dr));
        dr->is_clear    = 1;
        dr->rt_off      = rt;
        dr->rt_fmt      = st->surface_format;
        dr->rt_clip_w   = st->surface_clip_w;
        dr->rt_clip_h   = st->surface_clip_h;
        dr->clear_flags = flags;
        dr->clear_r = r; dr->clear_g = g; dr->clear_b = b; dr->clear_a = a;
        dr->clear_z = st->clear_z;
        dr->clear_s = st->clear_s;
        return;
    }"""

assert old_c21 in txt, "old_c21 not found"
txt = txt.replace(old_c21, new_c21, 1)

# 2. Quitar el bloqueo de rsx_present_flip_already_rendered para que el FLIP real de main.cpp siempre presente
txt = txt.replace(
    "if (clear_presents > 0 && s_d3d.draw_count < 1500) return 1;",
    "return 0;"
)

d3d_path.write_text(txt, encoding="latin-1")
print("[patch] d3d12_clear + Present unificados: todos los clears se ejecutan en orden y solo se presenta 1 vez por FLIP!")
