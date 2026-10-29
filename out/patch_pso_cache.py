from pathlib import Path
import re

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# Mostrar los valores actuales de *_SLOTS
for m in re.finditer(r"#define\s+(FP_PSO_SLOTS|VP_VS_SLOTS|VP_TEX_SLOTS|MAX_DRAWS)\s+\d+", txt):
    print("Antes:", m.group(0))

# Ampliar las tablas de cache de PSOs, Vertex Shaders, Texturas y Draws
txt = re.sub(r"#define\s+FP_PSO_SLOTS\s+\d+", "#define FP_PSO_SLOTS 4096", txt)
txt = re.sub(r"#define\s+VP_VS_SLOTS\s+\d+",  "#define VP_VS_SLOTS 1024", txt)
txt = re.sub(r"#define\s+VP_TEX_SLOTS\s+\d+", "#define VP_TEX_SLOTS 1024", txt)
txt = re.sub(r"#define\s+MAX_DRAWS\s+\d+",    "#define MAX_DRAWS 4096", txt)

for m in re.finditer(r"#define\s+(FP_PSO_SLOTS|VP_VS_SLOTS|VP_TEX_SLOTS|MAX_DRAWS)\s+\d+", txt):
    print("Ahora:", m.group(0))

d3d_path.write_text(txt, encoding="latin-1")
print("[patch] Cache de PSOs ampliado a 4096 slots (cero thrashing)!")
