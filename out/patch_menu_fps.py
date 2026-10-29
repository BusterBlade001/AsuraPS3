from pathlib import Path
import re

# --- 1. En cellSpurs.c: cachear trabajos ya ejecutados en jc_run_one_job y silenciar CreateTask ---
sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="latin-1")

old_jc_job = "    spu_workload_dispatch_job(vm_base + ea_bin, size_bin, job_ea, size_desc);\n}"
new_jc_job = """    {
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
    spu_workload_dispatch_job(vm_base + ea_bin, size_bin, job_ea, size_desc);
}"""

if "s_jcache[1024]" not in sp_txt and old_jc_job in sp_txt:
    sp_txt = sp_txt.replace(old_jc_job, new_jc_job, 1)
    print("[patch] cellSpurs.c: cache de descriptores activado en jc_run_one_job (elimina las 37,711 re-ejecuciones)!")

# Silenciar printf de CreateTask despues de 12 llamadas
sp_txt = re.sub(
    r'printf\("\[cellSpurs\] CreateTask\(id=%u,',
    r'{ static int _ctn=0; if (PS3_LOG_FIRST(_ctn, 12)) printf("[cellSpurs] CreateTask(id=%u,',
    sp_txt
)
sp_txt = sp_txt.replace(
    'context_ea, task_lsp[0], task_lsp[1], task_lsp[2], task_lsp[3]);\n',
    'context_ea, task_lsp[0], task_lsp[1], task_lsp[2], task_lsp[3]); }\n'
)
sp_path.write_text(sp_txt, encoding="latin-1")

# --- 2. En spu_workload.c: silenciar logs por trabajo ---
wl_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c")
wl_txt = wl_path.read_text(encoding="latin-1")

wl_txt = wl_txt.replace("int verbose = ps3_log_verbose();", "int verbose = 0;")
wl_txt = wl_txt.replace(
    'fprintf(stderr, "[taskset] built SpursTasksetContext image=%d "\n                            "taskset=0x%08X task=%u\\n", j->image_id,\n                            j->taskset_ea, j->taskid); fflush(stderr);',
    '{ static int _tcn=0; if (PS3_LOG_FIRST(_tcn, 12)) { fprintf(stderr, "[taskset] built SpursTasksetContext image=%d taskset=0x%08X task=%u\\n", j->image_id, j->taskset_ea, j->taskid); fflush(stderr); } }'
)
wl_txt = re.sub(
    r'fprintf\(stderr,\s*"\[spu_workload\] dispatch HIT \(async\)',
    r'if (0) fprintf(stderr, "[spu_workload] dispatch HIT (async)',
    wl_txt
)
wl_txt = re.sub(
    r'fprintf\(stderr,\s*"\[spu_workload\] async image=%d RETURNED',
    r'if (0) fprintf(stderr, "[spu_workload] async image=%d RETURNED',
    wl_txt
)
wl_path.write_text(wl_txt, encoding="latin-1")
print("[patch] spu_workload.c: silenciados los 105,000 logs por segundo!")
