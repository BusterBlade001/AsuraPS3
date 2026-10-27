from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# --- 1. Agregar tc3..tc7 (TEXCOORD3..7) a VSOutput en vp_translate_to_hlsl ---
old_vso = """        "struct VSOutput {\\n"
        "    float4 pos  : SV_POSITION;\\n"
        "    float4 col0 : COLOR0;\\n"
        "    float4 tc0  : TEXCOORD0;\\n"
        "    float4 norm : NORMAL;\\n"
        "    float4 tc1  : TEXCOORD1;\\n"
        "    float4 tc2  : TEXCOORD2;\\n"
        "};\\n"
        "VSOutput main(VSInput i) {\\n"
        "    float4 r[32];\\n"
        "    for (int k = 0; k < 32; k++) r[k] = float4(0,0,0,1);\\n"
        "    float4 o_pos = float4(0,0,0,1);\\n"
        "    float4 o_col0 = float4(1,1,1,1);\\n"
        "    float4 o_tc0 = float4(0,0,0,1);\\n"
        "    float4 o_tc1 = float4(0,0,0,1);\\n"
        "    float4 o_tc2 = float4(0,0,0,1);\\n"
        "    float4 tmp;\\n");"""

new_vso = """        "struct VSOutput {\\n"
        "    float4 pos  : SV_POSITION;\\n"
        "    float4 col0 : COLOR0;\\n"
        "    float4 tc0  : TEXCOORD0;\\n"
        "    float4 norm : NORMAL;\\n"
        "    float4 tc1  : TEXCOORD1;\\n"
        "    float4 tc2  : TEXCOORD2;\\n"
        "    float4 tc3  : TEXCOORD3;\\n"
        "    float4 tc4  : TEXCOORD4;\\n"
        "    float4 tc5  : TEXCOORD5;\\n"
        "    float4 tc6  : TEXCOORD6;\\n"
        "    float4 tc7  : TEXCOORD7;\\n"
        "};\\n"
        "VSOutput main(VSInput i) {\\n"
        "    float4 r[32];\\n"
        "    for (int k = 0; k < 32; k++) r[k] = float4(0,0,0,1);\\n"
        "    float4 o_pos = float4(0,0,0,1);\\n"
        "    float4 o_col0 = float4(1,1,1,1);\\n"
        "    float4 o_tc0 = float4(0,0,0,1);\\n"
        "    float4 o_tc1 = float4(0,0,0,1);\\n"
        "    float4 o_tc2 = float4(0,0,0,1);\\n"
        "    float4 o_tc3 = float4(0,0,0,1);\\n"
        "    float4 o_tc4 = float4(0,0,0,1);\\n"
        "    float4 o_tc5 = float4(0,0,0,1);\\n"
        "    float4 o_tc6 = float4(0,0,0,1);\\n"
        "    float4 o_tc7 = float4(0,0,0,1);\\n"
        "    float4 tmp;\\n");"""

old_vso_ret = """        "    VSOutput o;\\n"
        "    o.pos  = _p;\\n"
        "    o.col0 = o_col0;\\n"
        "    o.tc0  = o_tc0;\\n"
        "    o.norm = float4(0, 0, 1, 0);\\n"
        "    o.tc1  = o_tc1;\\n"
        "    o.tc2  = o_tc2;\\n"
        "    return o;\\n"
        "}\\n");"""

new_vso_ret = """        "    VSOutput o;\\n"
        "    o.pos  = _p;\\n"
        "    o.col0 = o_col0;\\n"
        "    o.tc0  = o_tc0;\\n"
        "    o.norm = float4(0, 0, 1, 0);\\n"
        "    o.tc1  = o_tc1;\\n"
        "    o.tc2  = o_tc2;\\n"
        "    o.tc3  = o_tc3;\\n"
        "    o.tc4  = o_tc4;\\n"
        "    o.tc5  = o_tc5;\\n"
        "    o.tc6  = o_tc6;\\n"
        "    o.tc7  = o_tc7;\\n"
        "    return o;\\n"
        "}\\n");"""

# Tambien mapear dst==10..14 en vp_translate_to_hlsl a o_tc3..o_tc7
old_dst9 = 'else if (dst == 9)  target = "o_tc2";'
new_dst9 = '''else if (dst == 9)  target = "o_tc2";
            else if (dst == 10) target = "o_tc3";
            else if (dst == 11) target = "o_tc4";
            else if (dst == 12) target = "o_tc5";
            else if (dst == 13) target = "o_tc6";
            else if (dst == 14) target = "o_tc7";'''

if old_vso in txt:
    txt = txt.replace(old_vso, new_vso, 1).replace(old_vso_ret, new_vso_ret, 1)
    if old_dst9 in txt:
        txt = txt.replace(old_dst9, new_dst9)
    d3d_path.write_text(txt, encoding="latin-1")
    print("[patch] VSOutput ahora exporta TEXCOORD0..TEXCOORD7 (tc0..tc7) igual que PSInput!")

lines = txt.splitlines()
print("\n=== rsx_d3d12_backend.c (3950..4320) ===")
for j in range(3950, min(len(lines), 4320)):
    print(f"{j+1:04d}: {lines[j]}")
