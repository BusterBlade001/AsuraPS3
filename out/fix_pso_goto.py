from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

old_block = """    ID3DBlob* pb = NULL; ID3DBlob* e = NULL;
    HRESULT hr = D3DCompile(hlsl, strlen(hlsl), "guest_fp", NULL, NULL,
                            "main", "ps_5_0", 0, 0, &pb, &e);
    if (FAILED(hr) || !pb) {
        static int _e2=0; if (PS3_LOG_FIRST(_e2, 16))
            printf("[FP] PS compile FAIL (fp=0x%08X): %s\\n", fp_addr,
                   e ? (const char*)e->lpVtbl->GetBufferPointer(e) : "?");
        if (e) e->lpVtbl->Release(e);
        return NULL;
    }"""

new_block = """    ID3D12PipelineState* pso = NULL;
    ID3DBlob* pb = NULL; ID3DBlob* e = NULL;
    HRESULT hr = D3DCompile(hlsl, strlen(hlsl), "guest_fp", NULL, NULL,
                            "main", "ps_5_0", 0, 0, &pb, &e);
    if (FAILED(hr) || !pb) {
        static int _e2=0; if (PS3_LOG_FIRST(_e2, 16))
            printf("[FP] PS compile FAIL (fp=0x%08X): %s\\n", fp_addr,
                   e ? (const char*)e->lpVtbl->GetBufferPointer(e) : "?");
        if (e) e->lpVtbl->Release(e);
        goto cache_pso_entry;
    }"""

old_tail = """    ID3D12PipelineState* pso = NULL;
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
    }
    { static int _ok=0; if (PS3_LOG_FIRST(_ok, 32)) printf("[FP] guest FP pipeline ready (fp=0x%08X)\\n", fp_addr); }
    rdoc_name((ID3D12Object*)pso, "pso fp 0x%08X ucode %08X vs %d", fp_addr, uhash, vs_idx);

    /* insert (evict oldest when full) */"""

new_tail = """    hr = s_d3d.device->lpVtbl->CreateGraphicsPipelineState(
        s_d3d.device, &pd, &IID_ID3D12PipelineState, (void**)&pso);
    if (FAILED(hr)) {
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
        pso = NULL;
        goto cache_pso_entry;
    }
    { static int _ok=0; if (PS3_LOG_FIRST(_ok, 32)) printf("[FP] guest FP pipeline ready (fp=0x%08X)\\n", fp_addr); }
    rdoc_name((ID3D12Object*)pso, "pso fp 0x%08X ucode %08X vs %d", fp_addr, uhash, vs_idx);

cache_pso_entry:
    /* insert (evict oldest when full) */"""

assert old_block in txt, "old_block not found"
assert old_tail in txt, "old_tail not found"
txt = txt.replace(old_block, new_block, 1).replace(old_tail, new_tail, 1)
d3d_path.write_text(txt, encoding="latin-1")
print("[patch] goto cache_pso_entry conectado con exito en rsx_d3d12_backend.c!")
