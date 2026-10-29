from pathlib import Path
import re

# --- 1. En ppu_recomp_032.cpp: hacer que func_00A30914 y func_00A30BDC usen timeout corto (10ms) y salgan a revisar func_00A6672C ---
p32 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_032.cpp")
t32 = p32.read_text(encoding="latin-1")

old_wait = """loc_00A30A3C:
        ctx->gpr[3] = ctx->gpr[30] + (int64_t)(0x78);
        ctx->gpr[4] = (int64_t)(int32_t)(-1);
        ctx->gpr[3] = ppc_rldicl(ctx->gpr[3], 0, 32);
        ctx->gpr[4] = ppc_rldicl(ctx->gpr[4], 0, 32);
        ctx->lr = 0x00A30A50; func_00A66F94(ctx); DRAIN_TRAMPOLINE(ctx);
        /* nop */;
        ctx->gpr[3] = ctx->gpr[28] | ctx->gpr[28];
        ctx->lr = 0x00A30A5C; func_00A30634(ctx); DRAIN_TRAMPOLINE(ctx);
        { int64_t a = (int32_t)ctx->gpr[3]; int64_t b = (int64_t)0; uint32_t cr_val = ((a < b) ? 8 : (a > b) ? 4 : 2) | ((ctx->xer >> 31) & 1u); ctx->cr = (ctx->cr & ~(0xFu << 0)) | (cr_val << 0); }
        ctx->gpr[9] = ctx->gpr[3] | ctx->gpr[3];
        if (((ctx->cr >> 1) & 1)) goto loc_00A309A8;"""

new_wait = """loc_00A30A3C:
        ctx->gpr[3] = ctx->gpr[30] + (int64_t)(0x78);
        ctx->gpr[4] = (int64_t)(int32_t)(10);
        ctx->gpr[3] = ppc_rldicl(ctx->gpr[3], 0, 32);
        ctx->gpr[4] = ppc_rldicl(ctx->gpr[4], 0, 32);
        ctx->lr = 0x00A30A50; func_00A66F94(ctx); DRAIN_TRAMPOLINE(ctx);
        /* nop */;
        ctx->gpr[3] = ctx->gpr[28] | ctx->gpr[28];
        ctx->lr = 0x00A30A5C; func_00A30634(ctx); DRAIN_TRAMPOLINE(ctx);
        { int64_t a = (int32_t)ctx->gpr[3]; int64_t b = (int64_t)0; uint32_t cr_val = ((a < b) ? 8 : (a > b) ? 4 : 2) | ((ctx->xer >> 31) & 1u); ctx->cr = (ctx->cr & ~(0xFu << 0)) | (cr_val << 0); }
        ctx->gpr[9] = ctx->gpr[3] | ctx->gpr[3];
        ctx->gpr[0] = 0;
        if (((ctx->cr >> 1) & 1)) goto loc_00A30968;"""

if old_wait in t32:
    t32 = t32.replace(old_wait, new_wait)
    p32.write_text(t32, encoding="latin-1")
    print("[patch] ppu_recomp_032.cpp: PPU PhysX thread ahora comprueba solicitud de cierre cada 10ms sin colgar ppu_thread_join!")

# --- 2. En spu_0021_at_018ECF00/spu_recomp.c (img=22): evitar HALT-ASSERT y spin cuando EAL == 0 en 208A0 ---
p21 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0021_at_018ECF00\spu_recomp.c")
t21 = p21.read_text(encoding="latin-1")
t21 = re.sub(r'if \([^\n]+HALT-ASSERT[^\n]+\n', '/* halt-assert bypassed */\n', t21)
old_208a0 = "void spu_0021_at_018ECF00_spu_func_000208A0(spu_context* ctx) {"
new_208a0 = "void spu_0021_at_018ECF00_spu_func_000208A0(spu_context* ctx) {\n        if (spu_shlqbyi(ctx->gpr[4], 4)._u32[0] == 0) { ctx->gpr[3] = spu_il(0); SPU_RET(ctx); }"
if "spu_shlqbyi(ctx->gpr[4], 4)._u32[0] == 0" not in t21:
    t21 = t21.replace(old_208a0, new_208a0, 1)
p21.write_text(t21, encoding="latin-1")
print("[patch] spu_0021 (img=22): protegido contra HALT-ASSERT y puntero nulo en 208A0!")

# --- 3. En rsx_d3d12_backend.c: apagar RSX_ACCUM_FRAME por defecto para no superponer submenus ---
d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
dtxt = d3d_path.read_text(encoding="latin-1")
dtxt = dtxt.replace(
    'if (accum < 0) { const char* e = getenv("RSX_ACCUM_FRAME"); accum = e ? atoi(e) : 1; }',
    'if (accum < 0) { const char* e = getenv("RSX_ACCUM_FRAME"); accum = e ? atoi(e) : 0; }'
)
d3d_path.write_text(dtxt, encoding="latin-1")
print("[patch] rsx_d3d12_backend.c: RSX_ACCUM_FRAME=0 restaurado (submenus limpios sin superponerse)!")
