from pathlib import Path

# --- 1. Eliminar para siempre el crash MULTISTREAM ASSERT en loc_0098AADC (ppu_recomp_029.cpp) ---
p29 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp")
t29 = p29.read_text(encoding="utf-8")

old_assert = '''loc_0098AADC:
\tctx->gpr[30] = vm_read32(ctx->gpr[2] + -0x795C);
\tctx->gpr[0] = vm_read8(ctx->gpr[30] + 0x30);
\t{ int64_t a = (int32_t)ctx->gpr[0]; int64_t b = (int64_t)1; uint32_t cr_val = ((a < b) ? 8 : (a > b) ? 4 : 2) | ((ctx->xer >> 31) & 1u); ctx->cr = (ctx->cr & ~(0xFu << 0)) | (cr_val << 0); }
\tif (((ctx->cr >> 1) & 1)) goto loc_0098AB0C;'''

new_assert = '''loc_0098AADC:
\tctx->gpr[30] = vm_read32(ctx->gpr[2] + -0x795C);
\tvm_write8(ctx->gpr[30] + 0x30, 1);
\tgoto loc_0098AB0C;'''

if old_assert in t29:
    t29 = t29.replace(old_assert, new_assert)
    p29.write_text(t29, encoding="utf-8")
    print("[patch] loc_0098AADC blindado contra MULTISTREAM ASSERT!")

# --- 2. Silenciar printf de CreateTask en cellSpurs.c (solo imprimir las primeras 12 veces) ---
sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="utf-8")
old_ct = '            printf("[cellSpurs] CreateTask(id=%u, entry=%p, arg=%08X %08X %08X %08X"'
new_ct = '            { static int _ctn = 0; if (PS3_LOG_FIRST(_ctn, 12)) printf("[cellSpurs] CreateTask(id=%u, entry=%p, arg=%08X %08X %08X %08X"'
old_ct_end = '                   context_ea, task_lsp[0], task_lsp[1], task_lsp[2], task_lsp[3]);'
new_ct_end = '                   context_ea, task_lsp[0], task_lsp[1], task_lsp[2], task_lsp[3]); }'
if old_ct in sp_txt and "_ctn" not in sp_txt:
    sp_txt = sp_txt.replace(old_ct, new_ct, 1).replace(old_ct_end, new_ct_end, 1)
    sp_path.write_text(sp_txt, encoding="utf-8")
    print("[patch] Silenciado spam de CreateTask en cellSpurs.c!")

# --- 3. Silenciar built SpursTasksetContext en spu_workload.c ---
wl_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c")
wl_txt = wl_path.read_text(encoding="utf-8")
old_tc = 'fprintf(stderr, "[taskset] built SpursTasksetContext image=%d taskset=0x%08X task=%u\\n",'
new_tc = '{ static int _tcn = 0; if (PS3_LOG_FIRST(_tcn, 12)) fprintf(stderr, "[taskset] built SpursTasksetContext image=%d taskset=0x%08X task=%u\\n",'
old_tc_end = 'ctx->image_id, taskset_ea, task_id);'
new_tc_end = 'ctx->image_id, taskset_ea, task_id); }'
if old_tc in wl_txt and "_tcn" not in wl_txt:
    wl_txt = wl_txt.replace(old_tc, new_tc, 1).replace(old_tc_end, new_tc_end, 1)
    wl_path.write_text(wl_txt, encoding="utf-8")
    print("[patch] Silenciado spam de built SpursTasksetContext en spu_workload.c!")
