from pathlib import Path

wl_path = Path(r"C:\AsuraPS3\ps3recomp\runtime\spu\spu_workload.c")
wl_txt = wl_path.read_text(encoding="latin-1")

# Quitar el reemplazo anterior y poner free(ls) solo en el cierre de spu_thread_entry
wl_txt = wl_txt.replace("if (!ts_slot || ts_slot->ls != ls) free(ls); free(j); return 0;", "free(j); return 0;")
wl_txt = wl_txt.replace(
    "/* Do NOT free(ls): a sibling task or late PPU reader may still touch\n     * the LS buffer after return; 256 KB per one-shot task is cheap. */\n    free(j);",
    "if (!ts_slot) free(ls);\n    free(j);"
)
wl_path.write_text(wl_txt, encoding="latin-1")
print("[patch] spu_workload.c corregido!")
