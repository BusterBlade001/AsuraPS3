from pathlib import Path

p29 = Path(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_029.cpp")
t29 = p29.read_text(encoding="latin-1")

# 1. Hacer que func_009935D4 (cellMSMP3Init) devuelva 0 (CELL_OK)
old_mp3 = "void func_009935D4(ppu_context* ctx) {"
new_mp3 = "void func_009935D4(ppu_context* ctx) {\n        ctx->gpr[3] = 0;\n        return;"
if "void func_009935D4(ppu_context* ctx) {\n        ctx->gpr[3] = 0;" not in t29:
    t29 = t29.replace(old_mp3, new_mp3, 1)
    print("[patch] func_009935D4 (cellMSMP3Init) -> CELL_OK (0)")

# 2. Hacer que func_0098A824 (cellMSSystemClose) devuelva 0 sin cerrar MultiStream
old_close = "void func_0098A824(ppu_context* ctx) {"
new_close = "void func_0098A824(ppu_context* ctx) {\n        ctx->gpr[3] = 0;\n        return;"
if "void func_0098A824(ppu_context* ctx) {\n        ctx->gpr[3] = 0;" not in t29:
    t29 = t29.replace(old_close, new_close, 1)
    print("[patch] func_0098A824 (cellMSSystemClose) -> no-op")

# 3. Neutralizar todas las puestas a 0 de +0x30 en cellMSSystemClose (incluyendo wrappers)
old_w30 = "        ctx->gpr[0] = (int64_t)(int32_t)(0);\n        ctx->gpr[3] = vm_read32(ctx->gpr[2] + -0x7870);\n        vm_write8(ctx->gpr[9] + 0x30, ctx->gpr[0]);"
new_w30 = "        ctx->gpr[3] = 0;\n        return;"
cnt_w30 = t29.count(old_w30)
t29 = t29.replace(old_w30, new_w30)
print(f"[patch] Neutralizados {cnt_w30} cierres de MultiStream (+0x30 = 0)")

# 4. Blindar loc_0098AADC (con 8 espacios exactos)
old_aadc = """loc_0098AADC:
        ctx->gpr[30] = vm_read32(ctx->gpr[2] + -0x795C);
        ctx->gpr[0] = vm_read8(ctx->gpr[30] + 0x30);
        { int64_t a = (int32_t)ctx->gpr[0]; int64_t b = (int64_t)1; uint32_t cr_val = ((a < b) ? 8 : (a > b) ? 4 : 2) | ((ctx->xer >> 31) & 1u); ctx->cr = (ctx->cr & ~(0xFu << 0)) | (cr_val << 0); }
        if (((ctx->cr >> 1) & 1)) goto loc_0098AB0C;"""

new_aadc = """loc_0098AADC:
        ctx->gpr[30] = vm_read32(ctx->gpr[2] + -0x795C);
        vm_write8(ctx->gpr[30] + 0x30, 1);
        goto loc_0098AB0C;"""

cnt_aadc = t29.count(old_aadc)
t29 = t29.replace(old_aadc, new_aadc)
p29.write_text(t29, encoding="latin-1")
print(f"[patch] Blindados {cnt_aadc} bloques loc_0098AADC en ppu_recomp_029.cpp!")

# 5. Ver spu_run_spurs_job en spu_workload.c
wl = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c").read_text(encoding="latin-1").splitlines()
for i, l in enumerate(wl):
    if "spu_run_spurs_job(" in l and i < 880:
        print(f"\n=== spu_run_spurs_job en spu_workload.c:{i+1} ===")
        for j in range(i, min(len(wl), i+75)):
            print(f"{j+1:04d}: {wl[j]}")
        break
