from pathlib import Path

# --- 1. Desactivar el hack YDKJ para image_id == 22 en runtime/spu/spu_workload.c ---
wl_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c")
wl_txt = wl_path.read_text(encoding="latin-1")

wl_txt = wl_txt.replace("if (j->image_id == 22 && getenv(\"YDKJ_CRI_TASKSET\"))", "if (0)")
wl_txt = wl_txt.replace("if (j->image_id == 22)", "if (0 /* disabled YDKJ hack */)")
wl_txt = wl_txt.replace("if (j->image_id != 22 && !getenv(\"LBP_NO_TASKSET\"))", "if (!getenv(\"LBP_NO_TASKSET\"))")
wl_path.write_text(wl_txt, encoding="latin-1")
print("[patch] spu_workload.c: desactivado el hack YDKJ que corrompia img=22 en el Episodio 1!")

# --- 2. Agregar cola sincronizada SPU->PPU (asura_spu_qpush16) en libs/spurs/cellSpurs.c ---
sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="latin-1")

old_qpop = """s32 cellSpursQueuePopBody(u64 queue_ea, u64 buffer_ea, u32 isPeek, u32 isBlocking)
{"""

new_qpop = """typedef struct {
    uint32_t queue_ea;
    uint8_t  data[16];
} AsuraQ16Item;

#define ASURA_Q16_CAP 256
static AsuraQ16Item       s_asura_q16[ASURA_Q16_CAP];
static uint32_t           s_asura_q16_head = 0;
static uint32_t           s_asura_q16_tail = 0;
static SRWLOCK            s_asura_q16_lock = SRWLOCK_INIT;
static CONDITION_VARIABLE s_asura_q16_cv   = CONDITION_VARIABLE_INIT;

void asura_spu_qpush16(uint32_t queue_ea, const uint8_t* src16)
{
    AcquireSRWLockExclusive(&s_asura_q16_lock);
    uint32_t idx = (s_asura_q16_tail++) % ASURA_Q16_CAP;
    s_asura_q16[idx].queue_ea = queue_ea;
    memcpy(s_asura_q16[idx].data, src16, 16);
    WakeAllConditionVariable(&s_asura_q16_cv);
    ReleaseSRWLockExclusive(&s_asura_q16_lock);
}

s32 cellSpursQueuePopBody(u64 queue_ea, u64 buffer_ea, u32 isPeek, u32 isBlocking)
{
    if (!queue_ea || !buffer_ea) return CELL_SPURS_TASK_ERROR_NULL_POINTER;
    u32 q_ check = (u32)queue_ea;
    u32 dst_check = (u32)buffer_ea;
    AcquireSRWLockExclusive(&s_asura_q16_lock);
    int waits = isBlocking ? 200 : 0;
    for (;;) {
        for (uint32_t i = s_asura_q16_head; i != s_asura_q16_tail; i++) {
            uint32_t idx = i % ASURA_Q16_CAP;
            if (s_asura_q16[idx].queue_ea == q_check || s_asura_q16[idx].queue_ea == 0) {
                memcpy(vm_base + dst_check, s_asura_q16[idx].data, 16);
                if (!isPeek) {
                    for (uint32_t j = i; j != s_asura_q16_head; j--)
                        s_asura_q16[j % ASURA_Q16_CAP] = s_asura_q16[(j - 1) % ASURA_Q16_CAP];
                    s_asura_q16_head++;
                }
                ReleaseSRWLockExclusive(&s_asura_q16_lock);
                return CELL_OK;
            }
        }
        if (waits-- <= 0) break;
        SleepConditionVariableSRW(&s_asura_q16_cv, &s_asura_q16_lock, 10, 0);
    }
    ReleaseSRWLockExclusive(&s_asura_q16_lock);
"""

if "asura_spu_qpush16" not in sp_txt:
    new_qpop = new_qpop.replace("u32 q_ check", "u32 q_check")
    assert old_qpop in sp_txt, "old_qpop not found"
    sp_txt = sp_txt.replace(old_qpop, new_qpop, 1)
    sp_path.write_text(sp_txt, encoding="latin-1")
    print("[patch] cellSpurs.c: asura_spu_qpush16 + cellSpursQueuePopBody bloqueante conectados!")

# --- 3. Conectar spu_func_0001FBD0 y spu_func_0001FBA8 en spu_0021_at_018ECF00 (img=22) ---
p21 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0021_at_018ECF00\spu_recomp.c")
t21 = p21.read_text(encoding="latin-1")

old_1fbd0 = "void spu_0021_at_018ECF00_spu_func_0001FBD0(spu_context* ctx) {"
new_1fbd0 = """extern void asura_spu_qpush16(uint32_t queue_ea, const uint8_t* src16);
void spu_0021_at_018ECF00_spu_func_0001FBD0(spu_context* ctx) {
        { uint32_t _qea = ctx->gpr[3]._u32[0] ? ctx->gpr[3]._u32[0] : spu_shlqbyi(ctx->gpr[3], 4)._u32[0];
          asura_spu_qpush16(_qea, ctx->ls + (ctx->gpr[4]._u32[0] & 0x3FFF0u));
          ctx->gpr[3] = spu_il(0);
          SPU_RET(ctx); }"""

old_1fba8 = "void spu_0021_at_018ECF00_spu_func_0001FBA8(spu_context* ctx) {"
new_1fba8 = """void spu_0021_at_018ECF00_spu_func_0001FBA8(spu_context* ctx) {
        ctx->gpr[3] = spu_il(0);
        SPU_RET(ctx);"""

if "asura_spu_qpush16" not in t21:
    assert old_1fbd0 in t21, "old_1fbd0 not found"
    assert old_1fba8 in t21, "old_1fba8 not found"
    t21 = t21.replace(old_1fbd0, new_1fbd0, 1).replace(old_1fba8, new_1fba8, 1)
    p21.write_text(t21, encoding="latin-1")
    print("[patch] spu_0021 (img=22): QueuePush conectado a asura_spu_qpush16!")
