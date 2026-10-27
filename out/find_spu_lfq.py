p = r"C:\AsuraPS3\ps3recomp\templates\project\spu\spu_0001_at_017C1F00\spu_recomp.c"
lines = open(p, "r", encoding="utf-8", errors="ignore").read().splitlines()

out = []
for i, l in enumerate(lines):
    if "9c80" in l.lower():
        # Buscar inicio y fin de esta única función
        start = i
        while start > 0 and not lines[start].startswith("void "):
            start -= 1
        end = i
        while end < len(lines) - 1 and not lines[end].startswith("}"):
            end += 1
        out.append(f"=== FUNCION EN {i+1} (lineas {start+1}..{end+1}) ===")
        for j in range(start, min(start + 160, end + 1)):
            out.append(f"{j+1:05d}: {lines[j]}")
        break

txt = "\n".join(out)
open(r"C:\AsuraPS3\out\spu_lfq.txt", "w", encoding="utf-8").write(txt)
print(txt)
