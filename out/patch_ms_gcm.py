from pathlib import Path
import re

# --- 1. Conectar EventFlagSet en spu_0000_at_017AA900/spu_recomp.c ---
p0 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0000_at_017AA900\spu_recomp.c")
t0 = p0.read_text(encoding="utf-8")

# Localizar la funcion que precede a spu_func_000165D0 (el entry de EventFlagSet en spu_0000)
m = re.search(r"(void spu_0000_at_017AA900_spu_func_00016[0-9A-F]{3}\(spu_context\* ctx\) \{\s+ctx->gpr\[5\] = spu_ori\(ctx->gpr\[3\], 0\);)", t0)
if m and "cellSpursEventFlagSet((void*)" not in t0:
    fn_hdr = m.group(1)
    hook = '''extern int32_t cellSpursEventFlagSet(void* eventFlag, uint16_t bits);
''' + fn_hdr.split("{")[0] + '''{
        cellSpursEventFlagSet((void*)(uintptr_t)ctx->gpr[3]._u32[0], (uint16_t)ctx->gpr[4]._u32[0]);
        ctx->gpr[3] = spu_il(0);
        SPU_RET(ctx);
        ctx->gpr[5] = spu_ori(ctx->gpr[3], 0);'''
    t0 = t0.replace(fn_hdr, hook, 1)
    p0.write_text(t0, encoding="utf-8")
    print("[patch] Conectado EventFlagSet en spu_0000:", fn_hdr.splitlines()[0])

# --- 2. En spu_workload.c y spu_channels.c: retornar a LR en llamadas a plugins no cargados (0x39818) ---
wl_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c")
wl_txt = wl_path.read_text(encoding="utf-8")

old_wl = '''        ctx->status = SPU_STATUS_STOPPED_BY_STOP;
        g_spu_trampoline_fn = NULL;
        return;'''

new_wl = '''        uint32_t ret_lr = ctx->gpr[0]._u32[0] & 0x3FFF8u;
        if (ret_lr >= 0x3000u && ret_lr < 0x20000u) {
            ctx->gpr[3]._u32[0] = 0; ctx->gpr[3]._u32[1] = 0; ctx->gpr[3]._u32[2] = 0; ctx->gpr[3]._u32[3] = 0;
            ctx->pc = ret_lr;
            g_spu_trampoline_fn = spu_lookup_func(ctx->image_id, ctx->pc);
            return;
        }
        ctx->status = SPU_STATUS_STOPPED_BY_STOP;
        g_spu_trampoline_fn = NULL;
        return;'''

if "ret_lr >= 0x3000u" not in wl_txt and old_wl in wl_txt:
    wl_txt = wl_txt.replace(old_wl, new_wl, 1)
    wl_path.write_text(wl_txt, encoding="utf-8")
    print("[patch] spu_workload.c: retorno limpio a LR en llamada a plugin ausente")

ch_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_channels.c")
ch_txt = ch_path.read_text(encoding="utf-8")
old_ch = '''          if (s_iu && w0) {
              static int _n = 0;
              if (PS3_LOG_FIRST(_n, 8))
                  fprintf(stderr, "[spu] img=%d interpreting unlifted LS 0x%05X "
                          "(runtime-loaded code)\\n", ctx->image_id, p);
              spu_interp_run(ctx, p);
              return;
          } }
        spu_halt(ctx);
        return;'''

new_ch = '''          if (w0) {
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
          } }
        spu_halt(ctx);
        return;'''

if "ret_lr >= 0x3000u" not in ch_txt and old_ch in ch_txt:
    ch_txt = ch_txt.replace(old_ch, new_ch, 1)
    ch_path.write_text(ch_txt, encoding="utf-8")
    print("[patch] spu_channels.c: activado interprete + retorno limpio a LR")

# --- 3. En cellSpurs.c: evitar bloqueo infinito en EventFlagWait ---
sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="utf-8")
old_ef = "static int s_force = -1;\n    if (s_force < 0) s_force = getenv(\"SPURS_EF_FORCE\") ? 1 : 0;"
new_ef = "static int s_force = 1;"
if old_ef in sp_txt:
    sp_txt = sp_txt.replace(old_ef, new_ef, 1)
    sp_txt = sp_txt.replace("if (s_force && waits >= 1000)", "if (s_force && waits >= 50)")
    sp_path.write_text(sp_txt, encoding="utf-8")
    print("[patch] cellSpurs.c: timeout de seguridad de 100ms en EventFlagWait activado")

# --- 4. En cellGcmSys.c: avanzar 4 bytes en jump-park de ShaderPatching en vez de saltar a put ---
gcm_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\cellGcmSys.c")
gcm_txt = gcm_path.read_text(encoding="utf-8")

old_park = '''                      } else if (now - park_since >= GCM_PARK_GRACE_MS) {
                          park_off = 0;
                          gcm_fifo_dump_around(s_fifo_getoff);
                          gcm_fifo_resync_why("jump-park", &s_fifo_getoff, put);
                      }'''

new_park = '''                      } else if (now - park_since >= 2) {
                          park_off = 0;
                          u32 next_ea = gcm_io2ea(s_fifo_getoff + 4);
                          u32 next_w  = next_ea ? vm_read32(next_ea) : 0;
                          if (s_fifo_getoff + 4 <= put && next_w != 0) {
                              /* Step over unpatched ShaderPatching self-jump so draw commands execute */
                              s_fifo_getoff += 4;
                              continue;
                          }
                          gcm_fifo_dump_around(s_fifo_getoff);
                          gcm_fifo_resync_why("jump-park", &s_fifo_getoff, put);
                      }'''

if old_park in gcm_txt:
    gcm_txt = gcm_txt.replace(old_park, new_park, 1)
    gcm_path.write_text(gcm_txt, encoding="utf-8")
    print("[patch] cellGcmSys.c: jump-park ahora avanza +4 bytes y ejecuta los comandos de dibujo!")
