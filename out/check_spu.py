import json
inv = json.load(open(r"C:\AsuraPS3\ps3recomp\templates\project\build\generated_spu\inventory.json"))
for i, p in enumerate(inv["programs"]):
    print(f"[{i:02d}] {p.get('name','')[:16]} status={p.get('status')} reason={p.get('reason')}")
