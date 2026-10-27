import json

path = r"C:\AsuraPS3\out\EBOOT.functions.json"
with open(path, "r") as f:
    data = json.load(f)

TEXT_END = 0x01606A10
flist = data["functions"] if isinstance(data, dict) and "functions" in data else data

cleaned = []
removed = 0
clamped = 0

for fn in flist:
    # Detectar llave de dirección
    k_addr = next((k for k in ("address", "addr", "start") if k in fn), None)
    raw_addr = fn[k_addr]
    addr = int(raw_addr, 16) if isinstance(raw_addr, str) else int(raw_addr)

    if addr >= TEXT_END:
        removed += 1
        continue

    if "size" in fn:
        raw_sz = fn["size"]
        sz = int(raw_sz, 16) if isinstance(raw_sz, str) else int(raw_sz)
        if addr + sz > TEXT_END:
            new_sz = TEXT_END - addr
            fn["size"] = f"0x{new_sz:X}" if isinstance(raw_sz, str) else new_sz
            clamped += 1
            print(f"Clamped func at 0x{addr:08X}: size {sz} -> {new_sz}")

    if "end" in fn:
        raw_end = fn["end"]
        end = int(raw_end, 16) if isinstance(raw_end, str) else int(raw_end)
        if end > TEXT_END:
            fn["end"] = f"0x{TEXT_END:08X}" if isinstance(raw_end, str) else TEXT_END
            clamped += 1
            print(f"Clamped func at 0x{addr:08X}: end 0x{end:08X} -> 0x{TEXT_END:08X}")

    cleaned.append(fn)

if isinstance(data, dict) and "functions" in data:
    data["functions"] = cleaned
else:
    data = cleaned

with open(path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Done! Kept {len(cleaned)} functions, clamped {clamped}, removed {removed} false functions >= 0x{TEXT_END:08X}")
