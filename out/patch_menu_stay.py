from pathlib import Path

# --- 1. En spu_0000: saltar solo la llamada a 0x39818 (_tg >= 0x1A3F0) en linea 676 ---
p0 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0000_at_017AA900\spu_recomp.c")
t0 = p0.read_text(encoding="utf-8")
old_676 = "{ uint32_t _tg = ctx->gpr[8]._u32[0]; ctx->gpr[0] = spu_link(0x3930); int32_t _si = (int32_t)ctx->image_id; ctx->pc = _tg; ctx->host_depth++; spu_indirect_branch(ctx); spu_drain_call(ctx, 0x3930); ctx->host_depth--; spu_img_restore(ctx, _si); }"
new_676 = "{ uint32_t _tg = ctx->gpr[8]._u32[0]; if (_tg < 0x1A3F0u) { ctx->gpr[0] = spu_link(0x3930); int32_t _si = (int32_t)ctx->image_id; ctx->pc = _tg; ctx->host_depth++; spu_indirect_branch(ctx); spu_drain_call(ctx, 0x3930); ctx->host_depth--; spu_img_restore(ctx, _si); } else { ctx->gpr[3] = spu_il(0); } }"
if old_676 in t0:
    t0 = t0.replace(old_676, new_676, 1)
    p0.write_text(t0, encoding="utf-8")
    print("[patch] spu_0000: llamada a 0x39818 protegida localmente sin tocar spu_channels.c!")

# --- 2. En ppu_recomp_029.cpp: evitar que func_0098A824 (cellMSSystemClose) apague MultiStream ---
p29 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp")
t29 = p29.read_text(encoding="utf-8")
old_close = "void func_0098A824(ppu_context* ctx) {"
new_close = "void func_0098A824(ppu_context* ctx) {\n\tctx->gpr[3] = 0;\n\treturn;"
if "void func_0098A824(ppu_context* ctx) {\n\tctx->gpr[3] = 0;" not in t29:
    assert old_close in t29, "func_0098A824 not found"
    t29 = t29.replace(old_close, new_close, 1)
    p29.write_text(t29, encoding="utf-8")
    print("[patch] func_0098A824 (cellMSSystemClose) blindado!")

# --- 3. Mostrar cómo rsx_d3d12_backend.c maneja bind_texture (fmt 0xA1 / B8) y draw_indexed ---
d3d = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c").read_text(encoding="utf-8", errors="ignore").splitlines()
for i, l in enumerate(d3d):
    if "bind_texture(" in l or "0x81" in l or "draw_indexed(" in l:
        print(f"\n=== rsx_d3d12_backend.c:{i+1} ===")
        for j in range(max(0, i-25), min(len(d3d), i+35)):
            print(f"{j+1:04d}: {d3d[j]}")
