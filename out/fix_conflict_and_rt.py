from pathlib import Path
import re

# --- 1. Verificar y aplicar fix limpio de jump-park en cellGcmSys.c ---
gcm_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\cellGcmSys.c")
gcm_txt = gcm_path.read_text(encoding="latin-1")

# Si quedara algun marcador de conflicto, limpiarlo quedandonos con nuestra rama
gcm_txt = re.sub(r"<<<<<<<[^\n]*\n(.*?)=======\n.*?>>>>>>>[^\n]*\n", r"\1", gcm_txt, flags=re.DOTALL)

old_park = '''                      } else if (now - park_since >= GCM_PARK_GRACE_MS) {
                          park_off = 0;
                          gcm_fifo_dump_around(s_fifo_getoff);
                          gcm_fifo_resync_why("jump-park", &s_fifo_getoff, put);
                      }'''

new_park = '''                      } else if (now - park_since >= 2) {
                          u32 next_ea = gcm_io2ea(s_fifo_getoff + 4);
                          u32 next_w  = next_ea ? vm_read32(next_ea) : 0;
                          park_off = 0;
                          if (s_fifo_getoff + 4 <= put && next_w != 0) {
                              s_fifo_getoff += 4;
                              continue;
                          }
                          gcm_fifo_dump_around(s_fifo_getoff);
                          gcm_fifo_resync_why("jump-park", &s_fifo_getoff, put);
                      }'''

if old_park in gcm_txt:
    gcm_txt = gcm_txt.replace(old_park, new_park, 1)
gcm_path.write_text(gcm_txt, encoding="latin-1")
print("[patch] cellGcmSys.c limpio sin conflictos Git!")

# --- 2. En rsx_d3d12_backend.c: enviar superficies finales 1280x720 RGBA8 al backbuffer ---
d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")
txt = re.sub(r"<<<<<<<[^\n]*\n(.*?)=======\n.*?>>>>>>>[^\n]*\n", r"\1", txt, flags=re.DOTALL)

old_by_size = """    { static int _bs = -1; if (_bs < 0) _bs = getenv("RT_DISPLAY_BY_SIZE") ? 1 : 0;
      if (_bs && st->color_target < 0x13 &&
          st->surface_clip_w == s_d3d.width && st->surface_clip_h == s_d3d.height)
          return 0; }"""

new_by_size = """    if (st->color_target < 0x13 &&
        st->surface_clip_w == s_d3d.width && st->surface_clip_h == s_d3d.height &&
        rsx_surface_dxgi(st->surface_format) == DXGI_FORMAT_R8G8B8A8_UNORM)
        return 0;"""

if old_by_size in txt:
    txt = txt.replace(old_by_size, new_by_size, 1)
    print("[patch] current_rt_off: superficies finales 1280x720 RGBA8 ahora van directo al backbuffer!")

# Y si un frame tiene solo draws offscreen, activar s_composite_src = 2 para que siempre presente el ultimo RT dibujado
old_pres = """    if (!has_display && !s_composite_src && s_d3d.draw_count == 0 && !env_accum)
        return;"""
new_pres = """    if (s_d3d.draw_count == 0 && !s_composite_src)
        return;
    if (!has_display && !s_composite_src && s_d3d.draw_count > 0)
        s_composite_src = 2;"""

if old_pres in txt:
    txt = txt.replace(old_pres, new_pres, 1)
    print("[patch] rsx_d3d12_backend_present: s_composite_src = 2 activado cuando !has_display!")

d3d_path.write_text(txt, encoding="latin-1")
