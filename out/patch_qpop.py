from pathlib import Path

# --- 1. Corregir lectura de EA de 64 bits en spu_0000 y spu_0001 ---
for spu_file in [
    r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0000_at_017AA900\spu_recomp.c",
    r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0001_at_017C1F00\spu_recomp.c"
]:
    p = Path(spu_file)
    t = p.read_text(encoding="utf-8")
    old_call = "cellSpursEventFlagSet((void*)(uintptr_t)ctx->gpr[3]._u32[0], (uint16_t)ctx->gpr[4]._u32[0]);"
    new_call = "{ uint32_t _ea = ctx->gpr[3]._u32[0] ? ctx->gpr[3]._u32[0] : spu_shlqbyi(ctx->gpr[3], 4)._u32[0]; cellSpursEventFlagSet((void*)(uintptr_t)_ea, (uint16_t)ctx->gpr[4]._u32[0]); }"
    if old_call in t:
        t = t.replace(old_call, new_call, 1)
        p.write_text(t, encoding="utf-8")
        print("[patch] EA 64-bit corregido en", p.parent.name)

# --- 2. En spu_channels.c y spu_workload.c: retornar exactamente a ret_lr con g_spu_trampoline_fn = NULL ---
ch_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_channels.c")
ch_txt = ch_path.read_text(encoding="utf-8")
old_ch_block = '''          if (w0) {
              static int _n = 0;
              if (PS3_LOG_FIRST(_n, 8))
                  fprintf(stderr, "[spu] img=%d interpreting unlifted LS 0x%05X "
                          "(runtime-loaded code)\\n", ctx->image_id, p);
              spu_interp_run(ctx, p);
              return;
          } }
        { uint32_t ret_lr = ctx->gpr[0]._u32[0] & SPU_LS_MASK;
          if (ret_lr >= 0x3000u && ret_lr < 0x20000u) {
              ctx->gpr[3]._u32[0] = 0;
              ctx->pc = ret_lr;
              g_spu_trampoline_fn = spu_lookup(ctx->pc, ctx->image_id);
              return;
          } }'''

new_ch_block = '''          (void)w0; }
        { uint32_t ret_lr = ctx->gpr[0]._u32[0] & SPU_LS_MASK;
          if (ret_lr >= 0x3000u && ret_lr < 0x20000u) {
              ctx->gpr[3]._u32[0] = 0; ctx->gpr[3]._u32[1] = 0; ctx->gpr[3]._u32[2] = 0; ctx->gpr[3]._u32[3] = 0;
              ctx->pc = ret_lr;
              g_spu_trampoline_fn = NULL;
              return;
          } }'''

if old_ch_block in ch_txt:
    ch_txt = ch_txt.replace(old_ch_block, new_ch_block, 1)
    ch_path.write_text(ch_txt, encoding="utf-8")
    print("[patch] spu_channels.c: retorno directo a spu_drain_call(ret_lr) sin corromper stack")

wl_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c")
wl_txt = wl_path.read_text(encoding="utf-8")
wl_txt = wl_txt.replace(
    "g_spu_trampoline_fn = spu_lookup_func(ctx->image_id, ctx->pc);",
    "g_spu_trampoline_fn = NULL;"
)
wl_path.write_text(wl_txt, encoding="utf-8")

# --- 3. En cellSpurs.h y cellSpurs.c: declarar e implementar cellSpursQueuePopBody y arreglar EventFlagWait ---
h_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.h")
h_txt = h_path.read_text(encoding="utf-8")
if "cellSpursQueuePopBody" not in h_txt:
    h_txt = h_txt.replace(
        "s32 cellSpursQueuePushBody(u64 queue_ea, u64 data_ea, u32 isBlocking);",
        "s32 cellSpursQueuePushBody(u64 queue_ea, u64 data_ea, u32 isBlocking);\ns32 cellSpursQueuePopBody(u64 queue_ea, u64 buffer_ea, u32 isPeek, u32 isBlocking);"
    )
    h_path.write_text(h_txt, encoding="utf-8")
    print("[patch] Declarado cellSpursQueuePopBody en cellSpurs.h")

sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="utf-8")

# Desactivar s_force global y solo permitir auto-signal en el flag de MultiStream (0x01B7AE80) si tarda >20ms
sp_txt = sp_txt.replace("static int s_force = 1;", "static int s_force = 0;")
sp_txt = sp_txt.replace(
    "if (s_force && waits >= 50)",
    "if ((ea == 0x01B7AE80u && waits >= 10) || (s_force && waits >= 1000))"
)

# Activar SPURS_QUEUE_PUSH por defecto en cellSpursQueuePushBody
sp_txt = sp_txt.replace(
    'if (s_exp < 0) s_exp = getenv("SPURS_QUEUE_PUSH") ? 1 : 0;',
    'if (s_exp < 0) s_exp = 1;'
)

# Implementar cellSpursQueuePopBody justo despues de cellSpursQueuePushBody
qpop_impl = '''
s32 cellSpursQueuePopBody(u64 queue_ea, u64 buffer_ea, u32 isPeek, u32 isBlocking)
{
    if (!queue_ea || !buffer_ea) return CELL_SPURS_TASK_ERROR_NULL_POINTER;
    u32 q   = (u32)queue_ea;
    u32 dst = (u32)buffer_ea;

    u32 head = vm_read32(q + 0x00);
    u32 tail = vm_read32(q + 0x04);
    u32 dep  = vm_read32(q + 0x0C);
    u32 sz   = vm_read32(q + 0x10);
    u32 buf  = (u32)vm_read64(q + 0x18);

    if (head == tail || dep == 0 || sz == 0 || buf == 0) {
        if (!isBlocking) {
            return (s32)0x80410901; /* CELL_SPURS_TASK_ERROR_AGAIN */
        }
        /* Brief wait if blocking, then return AGAIN if still empty */
        for (int w = 0; w < 5; w++) {
            Sleep(1);
            head = vm_read32(q + 0x00);
            tail = vm_read32(q + 0x04);
            if (head != tail) break;
        }
        if (head == tail) return (s32)0x80410901;
    }

    u32 slot = head % dep;
    memcpy(vm_base + dst, vm_base + buf + slot * sz, sz);
    if (!isPeek) {
        u32 nxt = (head + 1 < dep) ? head + 1 : 0;
        vm_write32(q + 0x00, nxt);
    }
    return CELL_OK;
}
'''

if "s32 cellSpursQueuePopBody(" not in sp_txt:
    anchor = "s32 cellSpursRequestIdleSpu(u64 spurs_ea)"
    assert anchor in sp_txt, "Anchor not found in cellSpurs.c"
    sp_txt = sp_txt.replace(anchor, qpop_impl + "\n" + anchor, 1)
    print("[patch] Implementado cellSpursQueuePopBody en cellSpurs.c")

sp_path.write_text(sp_txt, encoding="utf-8")
