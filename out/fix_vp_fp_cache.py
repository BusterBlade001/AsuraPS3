from pathlib import Path
import re

d3d_path = Path(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c")
txt = d3d_path.read_text(encoding="latin-1")

# 1. Limpiar los dos bloques fp_pso_n que dieron error de compilacion
txt = re.sub(r"\s*if \(s_d3d\.fp_pso_n < FP_PSO_SLOTS\) \{.*?\}\n", "\n", txt, flags=re.DOTALL)

# 2. Mostrar todas las macros *_CACHE / *_SLOTS actuales en rsx_d3d12_backend.c
for m in re.finditer(r"#define\s+(VP_[A-Z0-9_]+|MAX_DRAWS)\s+\d+", txt):
    print("Antes:", m.group(0))

# 3. Ampliar VP_FP_CACHE a 4096 y VP_VS_CACHE / VP_TEX_CACHE a 1024
txt = re.sub(r"(#define\s+VP_FP_CACHE\s+)\d+",  r"\g<1>4096", txt)
txt = re.sub(r"(#define\s+VP_VS_CACHE\s+)\d+",  r"\g<1>1024", txt)
txt = re.sub(r"(#define\s+VP_TEX_CACHE\s+)\d+", r"\g<1>1024", txt)

for m in re.finditer(r"#define\s+(VP_[A-Z0-9_]+|MAX_DRAWS)\s+\d+", txt):
    print("Ahora:", m.group(0))

d3d_path.write_text(txt, encoding="latin-1")
print("[patch] VP_FP_CACHE ampliado a 4096 ranuras y codigo limpio!")
