import glob

files = sorted(glob.glob(r"C:\AsuraPS3\ps3recomp\templates\project\recompiled\ppu_recomp_*.cpp"))

# 1. Encontrar qué func_ son los stubs de cellSysmoduleLoadModule (0x32267A31) y cellFsUnlink (0x7F4677A8)
stubs = {}
for path in files:
    txt = open(path, "r", encoding="utf-8", errors="ignore").read()
    for nid, name in [("0x32267A31", "cellSysmoduleLoadModule"), ("0x7F4677A8", "cellFsUnlink"), ("0x82F294B2", "cellOvisGetOverlayTableSize")]:
        if nid.lower() in txt.lower():
            lines = txt.splitlines()
            for i, l in enumerate(lines):
                if nid.lower() in l.lower():
                    for k in range(i, max(-1, i-10), -1):
                        if lines[k].startswith("void func_"):
                            fn = lines[k].split()[1].split("(")[0]
                            stubs[name] = fn
                            print(f"Stub {name} ({nid}) = {fn}")
                            break

# 2. Buscar dónde se llama a cellFsUnlink, cellOvis o func_008A9400
search_terms = list(stubs.values()) + ["func_008A9400", "func_0089B1CC"]
print("Buscando llamadas a:", search_terms)

for path in files:
    txt = open(path, "r", encoding="utf-8", errors="ignore").read()
    if not any(t in txt for t in search_terms):
        continue
    lines = txt.splitlines()
    for i, l in enumerate(lines):
        for t in search_terms:
            if t in l and not l.startswith(f"void {t}(") and "g_trampoline_fn" not in l and "function_table" not in l:
                print(f"\n=== CALL {t} in {path.split('\\')[-1]}:{i+1} ===")
                for j in range(max(0, i-20), min(len(lines), i+35)):
                    print(f"{j+1:06d}: {lines[j]}")
