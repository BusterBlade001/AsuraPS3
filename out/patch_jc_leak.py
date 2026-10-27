from pathlib import Path

sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="utf-8")

# 1. Evitar que jc_signal_done despierte por error a CellMemoryManager (q=4) y corrompa .bss
old_sig = "static void jc_signal_done(u32 jc_ea, int job_index)\n{"
new_sig = "static void jc_signal_done(u32 jc_ea, int job_index)\n{\n    (void)jc_ea; (void)job_index;\n    return;"
if "static void jc_signal_done(u32 jc_ea, int job_index)\n{\n    (void)jc_ea;" not in sp_txt:
    assert old_sig in sp_txt, "jc_signal_done not found"
    sp_txt = sp_txt.replace(old_sig, new_sig, 1)
    print("[patch] jc_signal_done silenciado: eliminada la fuga de 100 MB y la corrupcion de .bss en CellMemoryManager!")

# 2. Asegurar que SPURS_EF_FORCE esté completamente apagado
sp_txt = sp_txt.replace("if (s_force && waits >= 1000)", "if (0 && s_force && waits >= 1000)")
sp_path.write_text(sp_txt, encoding="utf-8")

# 3. Ver cómo rsx_d3d12_backend.c maneja d3d12_draw_arrays y la decompilacion FP
d3d = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c").read_text(encoding="utf-8", errors="ignore").splitlines()
print("\n=== rsx_d3d12_backend.c: d3d12_draw_arrays (6150..6265) ===")
for j in range(6150, 6265):
    print(f"{j+1:04d}: {d3d[j]}")
