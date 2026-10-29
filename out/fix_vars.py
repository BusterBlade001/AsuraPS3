from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

txt = txt.replace("s_d3d.fp_pso[slot].code_w0 = w0;", "s_d3d.fp_pso[slot].code_w0 = code[0];")
txt = txt.replace("s_d3d.fp_pso[slot].code_w1 = w1;", "s_d3d.fp_pso[slot].code_w1 = code[1];")
txt = txt.replace("s_d3d.fp_pso[slot].code_hash = ch;", "s_d3d.fp_pso[slot].code_hash = code_hash;")

d3d_path.write_text(txt, encoding="latin-1")
print("[patch] Variables code[0], code[1], code_hash corregidas en rsx_d3d12_backend.c!")
