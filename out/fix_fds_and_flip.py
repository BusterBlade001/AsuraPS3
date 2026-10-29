from pathlib import Path
import re

# --- 1. En runtime/ppu/ppu_fs.cpp: subir MAX_FDS de 48 a 2048 y activar _setmaxstdio(2048) ---
fs_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\ppu\ppu_fs.cpp")
fs_txt = fs_path.read_text(encoding="latin-1")

fs_txt = fs_txt.replace("#define MAX_FDS 48", "#define MAX_FDS 2048")
if "_setmaxstdio(2048)" not in fs_txt:
    fs_txt = fs_txt.replace(
        "void ppu_fs_register(void)\n{",
        "void ppu_fs_register(void)\n{\n    _setmaxstdio(2048);"
    )
fs_path.write_text(fs_txt, encoding="latin-1")
print("[patch] ppu_fs.cpp: MAX_FDS ampliado de 48 a 2048 (desbloquea la carga del Episodio 1)!")

# --- 2. En runtime/syscalls/sys_fs.c: subir SYS_FS_MAX_FD si existe ---
sfs_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\syscalls\sys_fs.c")
sfs_txt = sfs_path.read_text(encoding="latin-1")
sfs_txt = re.sub(r"(#define\s+SYS_FS_MAX_FD\s+)\d+", r"\g<1>2048", sfs_txt)
sfs_path.write_text(sfs_txt, encoding="latin-1")

# --- 3. En libs/video/rsx_d3d12_backend.c: sincronizar Present() con cellGcm_flip_request_count() ---
d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

old_flip_gate = """    {
        extern unsigned cellGcm_flip_request_count(void);
        if (rsx_present_flip_already_rendered(
                s_clear_presents, s_last_clear_presented_flip,
                cellGcm_flip_request_count()))
            return;
    }"""

new_flip_gate = """    {
        extern unsigned cellGcm_flip_request_count(void);
        static unsigned s_last_flip_present = 0;
        unsigned cur_fc = cellGcm_flip_request_count();
        if (rsx_present_flip_already_rendered(
                s_clear_presents, s_last_clear_presented_flip, cur_fc))
            return;
        /* Wait until the guest actually issues a FLIP before draining/presenting the frame,
         * so 60Hz frame_clock never splits a 30FPS guest frame into two half-built frames! */
        if (cur_fc != 0 && cur_fc == s_last_flip_present && s_d3d.draw_count < (MAX_DRAWS - 256))
            return;
        s_last_flip_present = cur_fc;
    }"""

if "s_last_flip_present" not in txt:
    assert old_flip_gate in txt, "old_flip_gate not found"
    txt = txt.replace(old_flip_gate, new_flip_gate, 1)
    d3d_path.write_text(txt, encoding="latin-1")
    print("[patch] rsx_d3d12_backend_present: sincronizado con el FLIP real del juego (cero parpadeo)!")
