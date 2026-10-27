from pathlib import Path

# --- 1. Regenerar templates/project/main.cpp limpio desde boot_main.cpp (sin <<<<<<< HEAD) ---
boot_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\ppu\tests\boot_main.cpp")
main_path = Path(r"C:\AsuraPS3\ps3recomp\templates\project\main.cpp")
btxt = boot_path.read_text(encoding="utf-8")

btxt = btxt.replace('#include "../ppu_tls.h"', '#include "ppu_tls.h"')
btxt = btxt.replace('#include "../../platform/win32_compat.h"', '#include "win32_compat.h"')
btxt = btxt.replace('#include "../../platform/win32_backtrace.h"', '#include "win32_backtrace.h"')
btxt = btxt.replace('#include "../../syscalls/sys_ppu_thread.h"', '#include "sys_ppu_thread.h"')
btxt = btxt.replace('void     ps3_load_prx_modules(void) __attribute__((weak));\nvoid     ps3_load_prx_modules(void) {}', 'void     ps3_load_prx_modules(void);')
btxt = btxt.replace('cellGame_init_from_paramsfo(sfo);', '/* cellGame_init_from_paramsfo(sfo); -- keep BLES00000 */')

main_path.write_text(btxt, encoding="utf-8")
print("[patch] templates/project/main.cpp regenerado limpio sin conflictos!")

# --- 2. Corregir llamada adelantada a rsx_surface_dxgi en rsx_d3d12_backend.c ---
d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

txt = txt.replace(
    "rsx_surface_dxgi(st->surface_format) == DXGI_FORMAT_R8G8B8A8_UNORM",
    "(st->surface_format != 0x0B && st->surface_format != 0x0C)"
)
d3d_path.write_text(txt, encoding="latin-1")
print("[patch] rsx_d3d12_backend.c corregido!")
