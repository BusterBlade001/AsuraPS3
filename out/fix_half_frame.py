from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# Evitar que rsx_d3d12_backend_present robe la mitad de los draws cuando la escena usa d3d12_clear (s_d3d.has_clear)
old_fn = """static int rsx_present_flip_already_rendered(unsigned clear_presents,
                                             unsigned last_clear_flip,
                                             unsigned cur_flip_count)
{
    return clear_presents > 0 && cur_flip_count == last_clear_flip;
}"""

new_fn = """static int rsx_present_flip_already_rendered(unsigned clear_presents,
                                             unsigned last_clear_flip,
                                             unsigned cur_flip_count)
{
    if (clear_presents > 0 && s_d3d.has_clear) return 1;
    return clear_presents > 0 && cur_flip_count == last_clear_flip;
}"""

if old_fn in txt:
    txt = txt.replace(old_fn, new_fn, 1)
    print("[patch] rsx_present_flip_already_rendered: bloqueado robo de draws a mitad de frame!")

# Y al terminar render_frame(), apagar has_clear para que si luego viene un video Bink puro sin clear, present() lo muestre
old_rf_end = "    s_d3d.draw_count = 0;\n    s_d3d.clear_count = 0;"
new_rf_end = "    s_d3d.draw_count = 0;\n    s_d3d.clear_count = 0;\n    s_d3d.has_clear = 0;"
if "s_d3d.has_clear = 0;" not in txt.split("static void render_frame")[1]:
    txt = txt.replace(old_rf_end, new_rf_end, 1)

d3d_path.write_text(txt, encoding="latin-1")
