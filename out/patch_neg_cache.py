from pathlib import Path

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# 1. En el bucle de búsqueda de s_d3d.fp_pso: si ya fue evaluado (incluso si pso == NULL por fallo), retornar de inmediato sin re-ejecutar D3DCompile!
old_lookup = """            s_d3d.fp_pso[i].cull == cull &&
            s_d3d.fp_pso[i].cube == cube_mask)
            return s_d3d.fp_pso[i].pso;"""

new_lookup = """            s_d3d.fp_pso[i].cull == cull &&
            s_d3d.fp_pso[i].cube == cube_mask)
            return s_d3d.fp_pso[i].pso;"""

# 2. Si D3DCompile o CreateGraphicsPipelineState falla, registrar la llave en s_d3d.fp_pso[slot] con pso = NULL para NO volver a llamar a D3DCompile cada frame!
old_d3d_fail = """    if (FAILED(hr) || !pb) {
        static int _e2=0; if (PS3_LOG_FIRST(_e2, 16))
            printf("[FP] PS compile FAIL (fp=0x%08X): %s\\n", fp_addr,
                   e ? (const char*)e->lpVtbl->GetBufferPointer(e) : "?");
        if (e) e->lpVtbl->Release(e);
        return NULL;
    }"""

new_d3d_fail = """    if (FAILED(hr) || !pb) {
        static int _e2=0; if (PS3_LOG_FIRST(_e2, 16))
            printf("[FP] PS compile FAIL (fp=0x%08X): %s\\n", fp_addr,
                   e ? (const char*)e->lpVtbl->GetBufferPointer(e) : "?");
        if (e) e->lpVtbl->Release(e);
        if (s_d3d.fp_pso_n < FP_PSO_SLOTS) {
            int slot = s_d3d.fp_pso_n++;
            s_d3d.fp_pso[slot].addr = fp_addr; s_d3d.fp_pso[slot].code_w0 = w0;
            s_d3d.fp_pso[slot].code_w1 = w1;   s_d3d.fp_pso[slot].code_hash = ch;
            s_d3d.fp_pso[slot].fp_hash = fp_hash; s_d3d.fp_pso[slot].vs_hash = vs_hash;
            s_d3d.fp_pso[slot].blend = blend;  s_d3d.fp_pso[slot].nrt = nrt;
            s_d3d.fp_pso[slot].rtfmt = (u32)rtfmt; s_d3d.fp_pso[slot].cmask = cmask;
            s_d3d.fp_pso[slot].cull = cull;    s_d3d.fp_pso[slot].zs = zs;
            s_d3d.fp_pso[slot].cube = cube_mask; s_d3d.fp_pso[slot].pso = NULL;
        }
        return NULL;
    }"""

old_pso_fail = """    if (FAILED(hr)) {
        static int _e3=0; if (PS3_LOG_FIRST(_e3, 16))
            printf("[FP] PSO FAIL (fp=0x%08X, 0x%08lX, vs=%d, blend=0x%X, nrt=%d, rtfmt=%d, cmask=0x%X)\\n",
                   fp_addr, hr, vs_idx, blend, nrt, (int)rtfmt, cmask);
        return NULL;
    }"""

new_pso_fail = """    if (FAILED(hr)) {
        static int _e3=0; if (PS3_LOG_FIRST(_e3, 16))
            printf("[FP] PSO FAIL (fp=0x%08X, 0x%08lX, vs=%d, blend=0x%X, nrt=%d, rtfmt=%d, cmask=0x%X)\\n",
                   fp_addr, hr, vs_idx, blend, nrt, (int)rtfmt, cmask);
        if (s_d3d.fp_pso_n < FP_PSO_SLOTS) {
            int slot = s_d3d.fp_pso_n++;
            s_d3d.fp_pso[slot].addr = fp_addr; s_d3d.fp_pso[slot].code_w0 = w0;
            s_d3d.fp_pso[slot].code_w1 = w1;   s_d3d.fp_pso[slot].code_hash = ch;
            s_d3d.fp_pso[slot].fp_hash = fp_hash; s_d3d.fp_pso[slot].vs_hash = vs_hash;
            s_d3d.fp_pso[slot].blend = blend;  s_d3d.fp_pso[slot].nrt = nrt;
            s_d3d.fp_pso[slot].rtfmt = (u32)rtfmt; s_d3d.fp_pso[slot].cmask = cmask;
            s_d3d.fp_pso[slot].cull = cull;    s_d3d.fp_pso[slot].zs = zs;
            s_d3d.fp_pso[slot].cube = cube_mask; s_d3d.fp_pso[slot].pso = NULL;
        }
        return NULL;
    }"""

assert old_d3d_fail in txt, "old_d3d_fail not found"
assert old_pso_fail in txt, "old_pso_fail not found"
txt = txt.replace(old_d3d_fail, new_d3d_fail, 1).replace(old_pso_fail, new_pso_fail, 1)
d3d_path.write_text(txt, encoding="latin-1")
print("[patch] Negative caching activado en vp_get_fp_pso: cero re-ejecuciones de D3DCompile!")
