from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# --- 1. En off_rt_get: no copiar basura cruda de vm_base + src al crear un Render Target ---
old_rt_init = "        if (vm_base && src != 0xFFFFFFFFu) {"
new_rt_init = "        if (0 && vm_base && src != 0xFFFFFFFFu) {"
if old_rt_init in txt:
    txt = txt.replace(old_rt_init, new_rt_init, 1)
    print("[patch] off_rt_get: desactivada copia de basura VRAM al inicializar Render Targets!")

# --- 2. En render_frame: desactivar copia de basura vm_base + disp_ea cuando draw_count == 0 ---
old_disp_raw = "    if (s_d3d.draw_count == 0 && s_present_this_frame) {"
new_disp_raw = "    if (0 && s_d3d.draw_count == 0 && s_present_this_frame) {"
if old_disp_raw in txt:
    txt = txt.replace(old_disp_raw, new_disp_raw, 1)
    print("[patch] render_frame: desactivada copia cruda de disp_ea cuando draw_count == 0!")

# --- 3. En rsx_d3d12_backend_present: ejecutar render_frame() en lotes offscreen para vaciar draw_count ---
old_pres_ret = """    if (!has_display && !s_composite_src && s_d3d.draw_count > 0 && !env_accum)
        return;"""
new_pres_ret = """    if (!has_display && !s_composite_src && s_d3d.draw_count == 0 && !env_accum)
        return;"""
if old_pres_ret in txt:
    txt = txt.replace(old_pres_ret, new_pres_ret, 1)
    print("[patch] rsx_d3d12_backend_present: lotes offscreen ahora ejecutan render_frame() y vacian draw_count!")

# --- 4. En vp_get_fp_pso: sanitizar factores BlendAlpha en D3D12 y fallback si falla PSO ---
old_blend = """    pd.BlendState.RenderTarget[0].BlendEnable    = (blend & 1) ? TRUE : FALSE;
    pd.BlendState.RenderTarget[0].SrcBlend       = (blend & 1) ? (D3D12_BLEND)((blend >> 1)  & 0x1F) : D3D12_BLEND_ONE;
    pd.BlendState.RenderTarget[0].DestBlend      = (blend & 1) ? (D3D12_BLEND)((blend >> 6)  & 0x1F) : D3D12_BLEND_ZERO;
    pd.BlendState.RenderTarget[0].BlendOp        = (blend & 1) ? (D3D12_BLEND_OP)((blend >> 21) & 0x7) : D3D12_BLEND_OP_ADD;
    pd.BlendState.RenderTarget[0].SrcBlendAlpha  = (blend & 1) ? (D3D12_BLEND)((blend >> 11) & 0x1F) : D3D12_BLEND_ONE;
    pd.BlendState.RenderTarget[0].DestBlendAlpha = (blend & 1) ? (D3D12_BLEND)((blend >> 16) & 0x1F) : D3D12_BLEND_ZERO;
    pd.BlendState.RenderTarget[0].BlendOpAlpha   = (blend & 1) ? (D3D12_BLEND_OP)((blend >> 24) & 0x7) : D3D12_BLEND_OP_ADD;"""

new_blend = """    pd.BlendState.RenderTarget[0].BlendEnable    = (blend & 1) ? TRUE : FALSE;
    {
        D3D12_BLEND sb  = (blend & 1) ? (D3D12_BLEND)((blend >> 1)  & 0x1F) : D3D12_BLEND_ONE;
        D3D12_BLEND db  = (blend & 1) ? (D3D12_BLEND)((blend >> 6)  & 0x1F) : D3D12_BLEND_ZERO;
        D3D12_BLEND_OP bop = (blend & 1) ? (D3D12_BLEND_OP)((blend >> 21) & 0x7) : D3D12_BLEND_OP_ADD;
        D3D12_BLEND sba = (blend & 1) ? (D3D12_BLEND)((blend >> 11) & 0x1F) : D3D12_BLEND_ONE;
        D3D12_BLEND dba = (blend & 1) ? (D3D12_BLEND)((blend >> 16) & 0x1F) : D3D12_BLEND_ZERO;
        D3D12_BLEND_OP bopa = (blend & 1) ? (D3D12_BLEND_OP)((blend >> 24) & 0x7) : D3D12_BLEND_OP_ADD;
        if (!sb) sb = D3D12_BLEND_ONE;
        if (!db) db = D3D12_BLEND_ZERO;
        if (!bop) bop = D3D12_BLEND_OP_ADD;
        if (!sba) sba = D3D12_BLEND_ONE;
        if (!dba) dba = D3D12_BLEND_ZERO;
        if (!bopa) bopa = D3D12_BLEND_OP_ADD;
        if (sba == D3D12_BLEND_SRC_COLOR) sba = D3D12_BLEND_SRC_ALPHA;
        else if (sba == D3D12_BLEND_INV_SRC_COLOR) sba = D3D12_BLEND_INV_SRC_ALPHA;
        else if (sba == D3D12_BLEND_DEST_COLOR) sba = D3D12_BLEND_DEST_ALPHA;
        else if (sba == D3D12_BLEND_INV_DEST_COLOR) sba = D3D12_BLEND_INV_DEST_ALPHA;
        if (dba == D3D12_BLEND_SRC_COLOR) dba = D3D12_BLEND_SRC_ALPHA;
        else if (dba == D3D12_BLEND_INV_SRC_COLOR) dba = D3D12_BLEND_INV_SRC_ALPHA;
        else if (dba == D3D12_BLEND_DEST_COLOR) dba = D3D12_BLEND_DEST_ALPHA;
        else if (dba == D3D12_BLEND_INV_DEST_COLOR) dba = D3D12_BLEND_INV_DEST_ALPHA;
        pd.BlendState.RenderTarget[0].SrcBlend       = sb;
        pd.BlendState.RenderTarget[0].DestBlend      = db;
        pd.BlendState.RenderTarget[0].BlendOp        = bop;
        pd.BlendState.RenderTarget[0].SrcBlendAlpha  = sba;
        pd.BlendState.RenderTarget[0].DestBlendAlpha = dba;
        pd.BlendState.RenderTarget[0].BlendOpAlpha   = bopa;
    }"""

old_pso_create = """    ID3D12PipelineState* pso = NULL;
    hr = s_d3d.device->lpVtbl->CreateGraphicsPipelineState(
        s_d3d.device, &pd, &IID_ID3D12PipelineState, (void**)&pso);
    pb->lpVtbl->Release(pb);
    if (FAILED(hr)) {
        static int _e3=0; if (PS3_LOG_FIRST(_e3, 16)) printf("[FP] PSO FAIL (fp=0x%08X, 0x%08lX)\\n", fp_addr, hr);
        return NULL;
    }"""

new_pso_create = """    ID3D12PipelineState* pso = NULL;
    hr = s_d3d.device->lpVtbl->CreateGraphicsPipelineState(
        s_d3d.device, &pd, &IID_ID3D12PipelineState, (void**)&pso);
    if (FAILED(hr)) {
        /* Fallback: if vs_idx == -1 had old VS signature, use first compiled guest VP or disable blend */
        if (vs_idx < 0 && s_d3d.vp_vs_n > 0 && s_d3d.vp_vs[0].vs) {
            pd.VS.pShaderBytecode = s_d3d.vp_vs[0].vs->lpVtbl->GetBufferPointer(s_d3d.vp_vs[0].vs);
            pd.VS.BytecodeLength  = s_d3d.vp_vs[0].vs->lpVtbl->GetBufferSize(s_d3d.vp_vs[0].vs);
        }
        for (int _r = 0; _r < (int)pd.NumRenderTargets; _r++)
            pd.BlendState.RenderTarget[_r].BlendEnable = FALSE;
        hr = s_d3d.device->lpVtbl->CreateGraphicsPipelineState(
            s_d3d.device, &pd, &IID_ID3D12PipelineState, (void**)&pso);
    }
    pb->lpVtbl->Release(pb);
    if (FAILED(hr)) {
        static int _e3=0; if (PS3_LOG_FIRST(_e3, 16))
            printf("[FP] PSO FAIL (fp=0x%08X, 0x%08lX, vs=%d, blend=0x%X, nrt=%d, rtfmt=%d, cmask=0x%X)\\n",
                   fp_addr, hr, vs_idx, blend, nrt, (int)rtfmt, cmask);
        return NULL;
    }"""

if old_blend in txt:
    txt = txt.replace(old_blend, new_blend, 1)
    print("[patch] vp_get_fp_pso: BlendState sanitizado para D3D12!")
if old_pso_create in txt:
    txt = txt.replace(old_pso_create, new_pso_create, 1)
    print("[patch] vp_get_fp_pso: fallback de PSO activado!")

d3d_path.write_text(txt, encoding="latin-1")
