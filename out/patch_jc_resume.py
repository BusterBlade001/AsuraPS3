from pathlib import Path

sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="latin-1")

# 1. Quitar s_jcache de jc_run_one_job para que jamas se salte un trabajo nuevo
old_jcache = """    {
        static struct { u32 ea; u64 hash; } s_jcache[1024];
        u32 csz = (size_desc && size_desc <= 256) ? size_desc : 256;
        u64 h = 1469598103934665603ULL;
        const u8* jb = vm_base + job_ea;
        for (u32 k = 0; k < csz; k++) h = (h ^ jb[k]) * 1099511628211ULL;
        u32 slot = (job_ea >> 7) & 1023u;
        if (s_jcache[slot].ea == job_ea && s_jcache[slot].hash == h)
            return;
        s_jcache[slot].ea = job_ea;
        s_jcache[slot].hash = h;
    }
    spu_workload_dispatch_job(vm_base + ea_bin, size_bin, job_ea, size_desc);"""

if old_jcache in sp_txt:
    sp_txt = sp_txt.replace(old_jcache, "    spu_workload_dispatch_job(vm_base + ea_bin, size_bin, job_ea, size_desc);", 1)
    print("[patch] Eliminado s_jcache!")

# 2. Guardar cur_pc al llegar a END en jc_execute para continuar desde el ultimo END sin re-ejecutar toda la historia
old_jc_exec = """static void jc_execute(u32 entry_ea, u32 jc_ea, u32 size_desc)
{
    u32 pc = entry_ea, ret_pc = 0;"""

new_jc_exec = """static u32 s_jc_last_end_pc[MAX_JOBCHAINS];

static void jc_execute(int slot, u32 entry_ea, u32 jc_ea, u32 size_desc)
{
    u32 pc = entry_ea, ret_pc = 0;
    if (s_jc_last_end_pc[slot] != 0) {
        u64 prev_end = vm_read64(s_jc_last_end_pc[slot]);
        /* If the game overwrote the previous END (0x7F) with a new command/NEXT, resume right there! */
        if ((prev_end & 127ULL) != (7ULL | (15ULL << 3)))
            pc = s_jc_last_end_pc[slot];
    }"""

old_jc_end = """            if (ext == (7 | (15 << 3))) {                     /* END */
                printf("[cellSpurs] chain 0x%08X: END after %d job(s)\\n", jc_ea, jobs);
                if (jobs) jc_signal_done(jc_ea, jobs - 1);
                return;
            }"""

new_jc_end = """            if (ext == (7 | (15 << 3))) {                     /* END */
                s_jc_last_end_pc[slot] = pc;
                if (jobs) jc_signal_done(jc_ea, jobs - 1);
                return;
            }"""

old_jc_call = """    jc_execute(s_jobchains[slot].entry_ea, s_jobchains[slot].jc_ea,
               s_jobchains[slot].size_desc);"""

new_jc_call = """    jc_execute(slot, s_jobchains[slot].entry_ea, s_jobchains[slot].jc_ea,
               s_jobchains[slot].size_desc);"""

if old_jc_exec in sp_txt:
    sp_txt = sp_txt.replace(old_jc_exec, new_jc_exec, 1)
    sp_txt = sp_txt.replace(old_jc_end, new_jc_end, 1)
    sp_txt = sp_txt.replace(old_jc_call, new_jc_call, 1)
    print("[patch] jc_execute ahora recuerda s_jc_last_end_pc y solo ejecuta los trabajos nuevos de cada frame!")

sp_path.write_text(sp_txt, encoding="latin-1")
