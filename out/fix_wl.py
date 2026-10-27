from pathlib import Path

wl_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c")
wl_txt = wl_path.read_text(encoding="utf-8")

old_wl = '''        ctx->status = SPU_STATUS_STOPPED_BY_STOP;
        g_spu_trampoline_fn = NULL;
        return;'''

new_wl = '''        uint32_t ret_lr = ctx->gpr[0]._u32[0] & 0x3FFF8u;
        if (ret_lr >= 0x3000u && ret_lr < 0x20000u) {
            ctx->gpr[3]._u32[0] = 0; ctx->gpr[3]._u32[1] = 0; ctx->gpr[3]._u32[2] = 0; ctx->gpr[3]._u32[3] = 0;
            ctx->pc = ret_lr;
            g_spu_trampoline_fn = NULL;
            return;
        }
        ctx->status = SPU_STATUS_STOPPED_BY_STOP;
        g_spu_trampoline_fn = NULL;
        return;'''

assert old_wl in wl_txt, "old_wl not found"
wl_txt = wl_txt.replace(old_wl, new_wl, 1)
wl_path.write_text(wl_txt, encoding="utf-8")
print("[patch] spu_workload.c corregido limpiamente")

sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="utf-8")
sp_txt = sp_txt.replace(
    "if ((ea == 0x01B7AE80u && waits >= 10) || (s_force && waits >= 1000))",
    "if (s_force && waits >= 1000)"
)
sp_path.write_text(sp_txt, encoding="utf-8")
print("[patch] cellSpurs.c: eliminado forzado artificial en EventFlagWait")
