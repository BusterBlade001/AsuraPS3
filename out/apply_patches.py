from pathlib import Path

# --- 1. Parchear runtime/ppu/ppu_fs.cpp ---
fs_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\ppu\ppu_fs.cpp")
fs_txt = fs_path.read_text(encoding="utf-8")

# Silenciar el spam masivo de '[fs] open' en /dev_hdd1/cache/
old_open_log = 'else fprintf(stderr, "[fs] open \'%s\' -> fd %d\\n", gpath, fd);'
new_open_log = '''else {
          static int s_cache_opens = 0;
          if (strncmp(gpath, "/dev_hdd1/cache/", 16) != 0 || ++s_cache_opens <= 6)
              fprintf(stderr, "[fs] open '%s' -> fd %d\\n", gpath, fd);
      }'''
if old_open_log in fs_txt:
    fs_txt = fs_txt.replace(old_open_log, new_open_log, 1)
    print("[patch] Silenciado spam de [fs] open para /dev_hdd1/cache/")

# Implementar cellFsRmdir, cellFsUnlink real y cellFsRename
old_unlink = '''static void cellFsRmdir(ppu_context* ctx)  { ctx->gpr[3] = CELL_OK; }
static void cellFsUnlink(ppu_context* ctx) { ctx->gpr[3] = CELL_OK; }'''

new_unlink = '''static void cellFsRmdir(ppu_context* ctx)
{
    char gpath[1024], hpath[1100];
    guest_strcpy(gpath, (uint32_t)ctx->gpr[3], sizeof gpath);
    host_path(hpath, sizeof hpath, gpath);
    _rmdir(hpath);
    ctx->gpr[3] = CELL_OK;
}
static void cellFsUnlink(ppu_context* ctx)
{
    char gpath[1024], hpath[1100];
    guest_strcpy(gpath, (uint32_t)ctx->gpr[3], sizeof gpath);
    host_path(hpath, sizeof hpath, gpath);
    int r = remove(hpath);
    fprintf(stderr, "[fs] unlink '%s' -> %s\\n", gpath, r == 0 ? "OK" : "ENOENT");
    ctx->gpr[3] = (r == 0) ? CELL_OK : (uint64_t)(int64_t)CELL_FS_ENOENT;
}
static void cellFsRename(ppu_context* ctx)
{
    char gfrom[1024], gto[1024], hfrom[1100], hto[1100];
    guest_strcpy(gfrom, (uint32_t)ctx->gpr[3], sizeof gfrom);
    guest_strcpy(gto,   (uint32_t)ctx->gpr[4], sizeof gto);
    host_path(hfrom, sizeof hfrom, gfrom);
    host_path(hto,   sizeof hto,   gto);
    remove(hto);
    int r = rename(hfrom, hto);
    fprintf(stderr, "[fs] rename '%s' -> '%s' (%s)\\n", gfrom, gto, r == 0 ? "OK" : "FAIL");
    ctx->gpr[3] = (r == 0) ? CELL_OK : (uint64_t)(int64_t)CELL_FS_ENOENT;
}'''

if old_unlink in fs_txt:
    fs_txt = fs_txt.replace(old_unlink, new_unlink, 1)
    print("[patch] Implementados cellFsRmdir, cellFsUnlink y cellFsRename")

old_reg = 'ps3_hle_register_ctx(ps3_compute_nid("cellFsUnlink"),   "cellFsUnlink",   cellFsUnlink);'
new_reg = old_reg + '\n    ps3_hle_register_ctx(ps3_compute_nid("cellFsRename"),   "cellFsRename",   cellFsRename);'
if "cellFsRename" not in fs_txt.split("ppu_fs_register")[1]:
    fs_txt = fs_txt.replace(old_reg, new_reg, 1)
    print("[patch] Registrado cellFsRename en ppu_fs_register")

fs_path.write_text(fs_txt, encoding="utf-8")

# --- 2. Actualizar templates/project/main.cpp con boot_main.cpp instrumentado ---
boot_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\ppu\tests\boot_main.cpp")
main_path = Path(r"C:\AsuraPS3\ps3recomp\templates\project\main.cpp")
btxt = boot_path.read_text(encoding="utf-8")

btxt = btxt.replace('#include "../ppu_tls.h"', '#include "ppu_tls.h"')
btxt = btxt.replace('#include "../../platform/win32_compat.h"', '#include "win32_compat.h"')
btxt = btxt.replace('#include "../../platform/win32_backtrace.h"', '#include "win32_backtrace.h"')
btxt = btxt.replace('#include "../../syscalls/sys_ppu_thread.h"', '#include "sys_ppu_thread.h"')
# stubs.cpp ya define ps3_load_prx_modules(), dejamos solo la declaracion
btxt = btxt.replace('void     ps3_load_prx_modules(void) __attribute__((weak));\nvoid     ps3_load_prx_modules(void) {}', 'void     ps3_load_prx_modules(void);')
# Mantener BLES00000 para conservar los 1.21 GB de .TFC ya instalados
btxt = btxt.replace('cellGame_init_from_paramsfo(sfo);', '/* cellGame_init_from_paramsfo(sfo); -- keep BLES00000 */')

main_path.write_text(btxt, encoding="utf-8")
print("[patch] main.cpp actualizado con cached_getenv, crash_filter, guest_prof y hang_watchdog!")
