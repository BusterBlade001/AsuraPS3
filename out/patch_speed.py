from pathlib import Path

sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
txt = sp_path.read_text(encoding="utf-8")

# 1. Apagar s_exp en cellSpursQueuePushBody para que image=23,18,16,15,14 no salgan ni se recreen 5681 veces
txt = txt.replace("if (s_exp < 0) s_exp = 1;", "if (s_exp < 0) s_exp = 0;")

# 2. Quitar la espera de 20ms en 0x01B7AE80 de EventFlagWait
txt = txt.replace(
    "if ((ea == 0x01B7AE80u && waits >= 10) || (s_force && waits >= 1000))",
    "if (0)"
)

# 3. En _cellSpursSendSignal: silenciar el printf masivo y despertar 0x01B7AE80 sin demora
old_sig = '''s32 _cellSpursSendSignal(void* taskset, u32 taskId)
{
    uint32_t taskset_ea = (uint32_t)(uintptr_t)taskset;
    printf("[cellSpurs] _SendSignal(taskset=0x%08X id=%u)\\n", taskset_ea, taskId);
    /* Real delivery now that SPU tasks execute (comment was stale). */
    if (taskset_ea) spu_taskset_signal_task(taskset_ea, taskId);
    return CELL_OK;
}'''

new_sig = '''s32 _cellSpursSendSignal(void* taskset, u32 taskId)
{
    uint32_t taskset_ea = (uint32_t)(uintptr_t)taskset;
    static int _n = 0;
    if (PS3_LOG_FIRST(_n, 8))
        printf("[cellSpurs] _SendSignal(taskset=0x%08X id=%u)\\n", taskset_ea, taskId);
    if (taskset_ea) spu_taskset_signal_task(taskset_ea, taskId);
    if (taskset_ea == 0x01B79500u)
        cellSpursEventFlagSet((CellSpursEventFlag*)(uintptr_t)0x01B7AE80u, 1);
    return CELL_OK;
}'''

if old_sig in txt:
    txt = txt.replace(old_sig, new_sig, 1)
    print("[patch] _cellSpursSendSignal optimizado y silenciado!")

sp_path.write_text(txt, encoding="utf-8")
print("[patch] cellSpurs.c actualizado!")
