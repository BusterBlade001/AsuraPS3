from pathlib import Path

# --- 1. Declarar _cellSpursLFQueuePushBody en libs/spurs/cellSpurs.h ---
h_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.h")
h_txt = h_path.read_text(encoding="utf-8")
decl = "s32 _cellSpursLFQueuePushBody(u64 queue_ea, u64 data_ea, u32 isBlocking);"
if "_cellSpursLFQueuePushBody" not in h_txt:
    h_txt = h_txt.replace(
        "s32 cellSpursLFQueueAttachLv2EventQueue(u64 queue_ea);",
        "s32 cellSpursLFQueueAttachLv2EventQueue(u64 queue_ea);\n" + decl
    )
    h_path.write_text(h_txt, encoding="utf-8")
    print("[patch] Declarado _cellSpursLFQueuePushBody en cellSpurs.h")

# --- 2. Implementar _cellSpursLFQueuePushBody y asura_spu_lfq_pop en libs/spurs/cellSpurs.c ---
c_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
c_txt = c_path.read_text(encoding="utf-8")

lfq_impl = '''
typedef struct {
    uint32_t queue_ea;
    uint8_t  data[32];
} AsuraLFQItem;

#define ASURA_LFQ_CAP 512
static AsuraLFQItem       s_asura_lfq[ASURA_LFQ_CAP];
static uint32_t           s_asura_lfq_head = 0;
static uint32_t           s_asura_lfq_tail = 0;
static SRWLOCK            s_asura_lfq_lock = SRWLOCK_INIT;
static CONDITION_VARIABLE s_asura_lfq_cv   = CONDITION_VARIABLE_INIT;

void asura_spu_lfq_pop(uint32_t queue_ea, uint8_t* dst32)
{
    AcquireSRWLockExclusive(&s_asura_lfq_lock);
    for (;;) {
        for (uint32_t i = s_asura_lfq_head; i != s_asura_lfq_tail; i++) {
            uint32_t idx = i % ASURA_LFQ_CAP;
            if (s_asura_lfq[idx].queue_ea == queue_ea) {
                memcpy(dst32, s_asura_lfq[idx].data, 32);
                for (uint32_t j = i; j != s_asura_lfq_head; j--) {
                    s_asura_lfq[j % ASURA_LFQ_CAP] = s_asura_lfq[(j - 1) % ASURA_LFQ_CAP];
                }
                s_asura_lfq_head++;
                ReleaseSRWLockExclusive(&s_asura_lfq_lock);
                return;
            }
        }
        SleepConditionVariableSRW(&s_asura_lfq_cv, &s_asura_lfq_lock, 1000, 0);
    }
}

s32 _cellSpursLFQueuePushBody(u64 queue_ea, u64 data_ea, u32 isBlocking)
{
    (void)isBlocking;
    if (!queue_ea || !data_ea) return CELL_SPURS_TASK_ERROR_NULL_POINTER;
    uint32_t q = (uint32_t)queue_ea;
    uint32_t d = (uint32_t)data_ea;

    static int _n = 0;
    if (_n < 40 || (_n % 250) == 0) {
        uint32_t src_ea  = vm_read32(d + 0x00);
        uint32_t dst_ea  = vm_read32(d + 0x04);
        uint32_t src_sz  = vm_read32(d + 0x08);
        uint32_t dst_sz  = vm_read32(d + 0x0C);
        uint32_t status  = vm_read32(d + 0x10);
        uint32_t flag_ea = vm_read32(d + 0x14);
        uint16_t bits    = vm_read16(d + 0x18);
        uint16_t pre     = vm_read16(d + 0x1A);
        uint16_t post    = vm_read16(d + 0x1C);
        fprintf(stderr, "[LFQPush#%d] q=0x%08X src=0x%08X(0x%X) -> dst=0x%08X(0x%X) status=0x%08X flag=0x%08X bits=0x%04X pre=%u post=%u\\n",
                _n, q, src_ea, src_sz, dst_ea, dst_sz, status, flag_ea, bits, pre, post);
        fflush(stderr);
    }
    _n++;

    AcquireSRWLockExclusive(&s_asura_lfq_lock);
    uint32_t idx = (s_asura_lfq_tail++) % ASURA_LFQ_CAP;
    s_asura_lfq[idx].queue_ea = q;
    memcpy(s_asura_lfq[idx].data, vm_base + d, 32);
    WakeAllConditionVariable(&s_asura_lfq_cv);
    ReleaseSRWLockExclusive(&s_asura_lfq_lock);
    return CELL_OK;
}
'''

if "_cellSpursLFQueuePushBody" not in c_txt:
    anchor = "s32 cellSpursLFQueueAttachLv2EventQueue(u64 queue_ea)\n{\n    static int _n = 0;\n    if (PS3_LOG_FIRST(_n, 8)) printf(\"[cellSpurs] LFQueueAttachLv2EventQueue(q=0x%08X)\\n\", (u32)queue_ea);\n    return CELL_OK;\n}"
    assert anchor in c_txt, "Anchor not found in cellSpurs.c"
    c_txt = c_txt.replace(anchor, anchor + "\n" + lfq_impl, 1)
    c_path.write_text(c_txt, encoding="utf-8")
    print("[patch] Implementado _cellSpursLFQueuePushBody en cellSpurs.c")

# --- 3. Conectar spu_0001_at_017C1F00/spu_recomp.c ---
spu_path = Path(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0001_at_017C1F00\spu_recomp.c")
spu_txt = spu_path.read_text(encoding="utf-8")

old_31a0 = '''void spu_0001_at_017C1F00_spu_func_000031A0(spu_context* ctx) {
        ctx->gpr[3] = spu_ori(ctx->gpr[90], 0);
        ctx->gpr[4] = spu_ai(ctx->gpr[1], 32);
        ctx->gpr[5] = spu_il(1);
        ctx->gpr[0] = spu_link(0x31B0); { int32_t _si = (int32_t)ctx->image_id; ctx->host_depth++; spu_0001_at_017C1F00_spu_func_00009CB0(ctx); spu_drain_call(ctx, 0x31B0); ctx->host_depth--; spu_img_restore(ctx, _si); }
        if (ctx->gpr[3]._u32[0] != 0) { ctx->pc = 0x3304; g_spu_trampoline_fn = spu_0001_at_017C1F00_spu_func_00003304; return; }
        { ctx->pc = 0x31B4; g_spu_trampoline_fn = spu_0001_at_017C1F00_spu_func_000031B4; return; }
}'''

new_31a0 = '''extern void asura_spu_lfq_pop(uint32_t queue_ea, uint8_t* dst32);
extern int32_t cellSpursEventFlagSet(void* eventFlag, uint16_t bits);

void spu_0001_at_017C1F00_spu_func_000031A0(spu_context* ctx) {
        asura_spu_lfq_pop(ctx->gpr[90]._u32[0], ctx->ls + ctx->gpr[1]._u32[0] + 0x30);
        { ctx->pc = 0x31C8; g_spu_trampoline_fn = spu_0001_at_017C1F00_spu_func_000031C8; return; }
}'''

old_32d0 = '''void spu_0001_at_017C1F00_spu_func_000032D0(spu_context* ctx) {
        ctx->gpr[0] = spu_link(0x32D4); { int32_t _si = (int32_t)ctx->image_id; ctx->host_depth++; spu_0001_at_017C1F00_spu_func_000095D0(ctx); spu_drain_call(ctx, 0x32D4); ctx->host_depth--; spu_img_restore(ctx, _si); }'''

new_32d0 = '''void spu_0001_at_017C1F00_spu_func_000032D0(spu_context* ctx) {
        { ctx->pc = 0x31A0; g_spu_trampoline_fn = spu_0001_at_017C1F00_spu_func_000031A0; return; }
        ctx->gpr[0] = spu_link(0x32D4); { int32_t _si = (int32_t)ctx->image_id; ctx->host_depth++; spu_0001_at_017C1F00_spu_func_000095D0(ctx); spu_drain_call(ctx, 0x32D4); ctx->host_depth--; spu_img_restore(ctx, _si); }'''

old_9688 = '''void spu_0001_at_017C1F00_spu_func_00009688(spu_context* ctx) {
        ctx->gpr[5] = spu_ori(ctx->gpr[3], 0);'''

new_9688 = '''void spu_0001_at_017C1F00_spu_func_00009688(spu_context* ctx) {
        cellSpursEventFlagSet((void*)(uintptr_t)ctx->gpr[3]._u32[0], (uint16_t)ctx->gpr[4]._u32[0]);
        ctx->gpr[3] = spu_il(0);
        SPU_RET(ctx);
        ctx->gpr[5] = spu_ori(ctx->gpr[3], 0);'''

if "asura_spu_lfq_pop" not in spu_txt:
    assert old_31a0 in spu_txt, "old_31a0 not found"
    assert old_32d0 in spu_txt, "old_32d0 not found"
    assert old_9688 in spu_txt, "old_9688 not found"
    spu_txt = spu_txt.replace(old_31a0, new_31a0, 1)
    spu_txt = spu_txt.replace(old_32d0, new_32d0, 1)
    spu_txt = spu_txt.replace(old_9688, new_9688, 1)
    spu_path.write_text(spu_txt, encoding="utf-8")
    print("[patch] Conectado spu_0001 (31A0, 32D0, 9688) a asura_spu_lfq_pop y cellSpursEventFlagSet")
