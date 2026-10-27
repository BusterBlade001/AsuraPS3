from pathlib import Path

sfs_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\syscalls\sys_fs.c")
txt = sfs_path.read_text(encoding="utf-8")

old_root = '''    if (g_sys_fs_root[0] == '.' && g_sys_fs_root[1] == '\\0') {
        const char* env = getenv("PS3_VFS_ROOT");
        if (env && *env) { strncpy(g_sys_fs_root, env, sizeof(g_sys_fs_root) - 1); g_sys_fs_root[sizeof(g_sys_fs_root)-1] = 0; }
    }'''

new_root = '''    if (g_sys_fs_root[0] == '.' && g_sys_fs_root[1] == '\\0') {
        extern const char* ppu_vfs_root;
        const char* env = getenv("PS3_VFS_ROOT");
        if (!env || !*env) env = ppu_vfs_root;
        if (env && *env) { strncpy(g_sys_fs_root, env, sizeof(g_sys_fs_root) - 1); g_sys_fs_root[sizeof(g_sys_fs_root)-1] = 0; }
    }'''

if "extern const char* ppu_vfs_root;" not in txt:
    assert old_root in txt, "old_root not found in sys_fs.c"
    txt = txt.replace(old_root, new_root, 1)
    sfs_path.write_text(txt, encoding="utf-8")
    print("[patch] sys_fs.c conectado a ppu_vfs_root!")
