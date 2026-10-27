d3d = open(r"C:\AsuraPS3\ps3recomp\libs\video\rsx_d3d12_backend.c", "r", encoding="latin-1").read().splitlines()
out = []
out.append("=== 1. vp_upload_tex_slot y swizzle (2420..2600) ===")
for j in range(2420, 2600):
    out.append(f"{j+1:04d}: {d3d[j]}")

out.append("\n=== 2. composite_present y pre-pass de RTs (3675..4495) ===")
for j in range(3675, 4495):
    out.append(f"{j+1:04d}: {d3d[j]}")

b20 = open(r"C:\AsuraPS3\out\boot20.log", "r", encoding="latin-1").read().splitlines()
out.append("\n=== 3. Lineas [FP], offscreen RT y BIK en boot20.log ===")
for i, l in enumerate(b20):
    if any(k in l for k in ("[FP]", "offscreen RT", ".BIK", "PSO FAIL")):
        out.append(f"[{i:05d}] {l[:115]}")

txt = "\n".join(out)
open(r"C:\AsuraPS3\out\d3d_mid.txt", "w", encoding="utf-8").write(txt)
print("Guardado en C:\\AsuraPS3\\out\\d3d_mid.txt (lineas:", len(out), ")")
for l in out[-45:]:
    print(l)
