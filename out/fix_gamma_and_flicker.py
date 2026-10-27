from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# --- 1. Desactivar la distorsion pow(x, 2.2) (rsx_srgb) sobre planos YCrCb de Bink y texturas ---
old_srgb = 'if (s_srgb < 0) s_srgb = getenv("NO_SRGB_TEX") ? 0 : 1;'
new_srgb = 'if (s_srgb < 0) s_srgb = 0;'
if old_srgb in txt:
    txt = txt.replace(old_srgb, new_srgb, 1)
    print("[patch] 1. s_srgb = 0: eliminada distorsion pow(2.2) sobre planos YCrCb y texturas!")

# --- 2. Mantener 0xABF0000 y 0xBDF0000 como Render Targets en off_rt[] para no perder el fondo del menu ---
old_by_size = """    if (st->color_target < 0x13 &&
        st->surface_clip_w == s_d3d.width && st->surface_clip_h == s_d3d.height &&
        (st->surface_format != 0x0B && st->surface_format != 0x0C))
        return 0;"""

new_by_size = """    { static int _bs = -1; if (_bs < 0) _bs = getenv("RT_DISPLAY_BY_SIZE") ? 1 : 0;
      if (_bs && st->color_target < 0x13 &&
          st->surface_clip_w == s_d3d.width && st->surface_clip_h == s_d3d.height)
          return 0; }"""

if old_by_size in txt:
    txt = txt.replace(old_by_size, new_by_size, 1)
    print("[patch] 2. current_rt_off: 0xABF0000 y 0xBDF0000 preservados en off_rt[] como texturas del menu!")

# --- 3. Eliminar el doble Present() (15 FPS / parpadeo negro) en lotes offscreen ---
old_pres = """    if (s_d3d.draw_count == 0 && !s_composite_src)
        return;
    if (!has_display && !s_composite_src && s_d3d.draw_count > 0)
        s_composite_src = 2;"""

new_pres = """    if (s_d3d.draw_count == 0 && !s_composite_src)
        return;"""

if old_pres in txt:
    txt = txt.replace(old_pres, new_pres, 1)
    print("[patch] 3. rsx_d3d12_backend_present: eliminado doble Present() en negro!")

old_clr = "    s_d3d.cmd_list->lpVtbl->ClearRenderTargetView(s_d3d.cmd_list, rtv_handle, clear, 0, NULL);\n    if (s_d3d.depth_buffer)"
new_clr = "    if (s_present_this_frame)\n        s_d3d.cmd_list->lpVtbl->ClearRenderTargetView(s_d3d.cmd_list, rtv_handle, clear, 0, NULL);\n    if (s_d3d.depth_buffer)"
if old_clr in txt:
    txt = txt.replace(old_clr, new_clr, 1)
    print("[patch] 4. render_frame: el backbuffer solo se limpia cuando s_present_this_frame == 1!")

d3d_path.write_text(txt, encoding="latin-1")
