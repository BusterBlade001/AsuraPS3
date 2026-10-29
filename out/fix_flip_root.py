from pathlib import Path
import glob

# --- 1. En cellGcmSys.c: evitar que FlipPump (cellGcmSetFlipImmediate(0)) machaque el bufferId de cellGcmSetPrepareFlip ---
gcm_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\cellGcmSys.c")
gtxt = gcm_path.read_text(encoding="latin-1")

old_imm = """s32 cellGcmSetFlipImmediate(u32 bufferId)
{
    printf("[cellGcmSys] SetFlipImmediate(bufferId=%u)\\n", bufferId);
    return cellGcmSetFlipCommand(bufferId);
}"""

new_imm = """s32 cellGcmSetFlipImmediate(u32 bufferId)
{
    (void)bufferId;
    s_flip_status = CELL_GCM_FLIP_STATUS_DONE;
    return CELL_OK;
}"""

assert old_imm in gtxt, "old_imm not found in cellGcmSys.c"
gtxt = gtxt.replace(old_imm, new_imm, 1)
gcm_path.write_text(gtxt, encoding="latin-1")
print("[patch] cellGcmSys.c: cellGcmSetFlipImmediate(0) ya no machaca el bufferId ni duplica los flips!")

# --- 2. En rsx_d3d12_backend.c: presentar exactamente 1 vez por cada cellGcmSetPrepareFlip (s_flip_request_count) ---
d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
dtxt = d3d_path.read_text(encoding="latin-1")

# En d3d12_clear: encolar siempre el clear en su posicion exacta sin llamar a render_frame() a mitad de frame
old_dclear = """        if (s_d3d.initialized) {
            s_present_this_frame = 1;
            render_frame();
            s_clear_presents++;
            {
                extern unsigned cellGcm_flip_request_count(void);
                s_last_clear_presented_flip = cellGcm_flip_request_count();
            }
        }
        s_d3d.draw_count = 0;
        s_d3d.clear_count = 0;"""

new_dclear = """        if (s_d3d.clear_count < MAX_CLEARS) {
            ClearCmd* cc = &s_d3d.clears[s_d3d.clear_count++];
            cc->rt_off = 0; cc->before_draw = s_d3d.draw_count;
            cc->mask = mask;
            cc->r = r; cc->g = g; cc->b = b; cc->a = a;
        }
        return;"""

if old_dclear in dtxt:
    dtxt = dtxt.replace(old_dclear, new_dclear, 1)
    print("[patch] d3d12_clear: ya no parte el frame en dos!")

# En rsx_d3d12_backend_present: presentar unicamente cuando cellGcmSetPrepareFlip haya avanzado cur_fc
old_pres_gate = """        (void)s_last_flip_present;"""
new_pres_gate = """        if (cur_fc != 0 && cur_fc == s_last_flip_present)
            return;
        s_last_flip_present = cur_fc;"""

if old_pres_gate in dtxt:
    dtxt = dtxt.replace(old_pres_gate, new_pres_gate, 1)
    print("[patch] rsx_d3d12_backend_present: sincronizado 1:1 con cellGcmSetPrepareFlip (30 FPS clavados)!")

d3d_path.write_text(dtxt, encoding="latin-1")

# --- 3. Mostrar func_00AEEFE4 (donde salio 0x007A120C al cargar el Episodio 1) ---
for p in sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp")):
    txt = open(p, "r", encoding="latin-1").read()
    if "void func_00AEEFE4(" in txt:
        lines = txt.splitlines()
        for i, l in enumerate(lines):
            if "void func_00AEEFE4(" in l:
                print(f"\n=== func_00AEEFE4 en {p.split('\\')[-1]}:{i+1} ===")
                for j in range(i, min(len(lines), i+95)):
                    print(f"{j+1:06d}: {lines[j]}")
                break
