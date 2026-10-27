from pathlib import Path

# 1. Agregar el stub de cellSysutilNpEulaCheck en templates/project/stubs.cpp para que lld-link enlace limpio
stubs_path = Path(r"C:\AsuraPS3\ps3recomp\templates\project\stubs.cpp")
stxt = stubs_path.read_text(encoding="utf-8")
if "cellSysutilNpEulaCheck" not in stxt:
    stxt += '\nextern "C" int cellSysutilNpEulaCheck(void) { return 0; }\n'
    stubs_path.write_text(stxt, encoding="utf-8")
    print("[patch] Agregado stub cellSysutilNpEulaCheck en stubs.cpp!")

# 2. Auditoria rapida para confirmar que todos nuestros parches siguen intactos tras el git pull
checks = [
    ("cellOvis.c (Return 0)", r"libs\misc\cellOvis.c", "return 0;"),
    ("cellSpurs.c (HLE Zlib)", r"libs\spurs\cellSpurs.c", "asura_inflate_raw"),
    ("cellSpurs.c (QueuePopBody)", r"libs\spurs\cellSpurs.c", "cellSpursQueuePopBody"),
    ("sceNpTrophy.c (Big-Endian)", r"libs\network\sceNpTrophy.c", "vm_write32(details_ea + 0x00, 32)"),
    ("sys_fs.c (ppu_vfs_root)", r"runtime\syscalls\sys_fs.c", "ppu_vfs_root"),
    ("cellGcmSys.c (jump-park +4)", r"libs\video\cellGcmSys.c", "s_fifo_getoff += 4;"),
    ("rsx_d3d12_backend.c (VSOutput tc7)", r"libs\video\rsx_d3d12_backend.c", "o_tc7"),
    ("spu_workloads.c (29 SPU images)", r"templates\project\spu\spu_workloads.c", "spujob_D6E964B601AB14C0"),
]
print("\n=== AUDITORIA DE PARCHES EN C:\\AsuraPS3\\ps3recomp ===")
for label, rel, needle in checks:
    p = Path(r"C:\AsuraPS3\ps3recomp") / rel
    ok = p.exists() and (needle in p.read_text(encoding="latin-1"))
    print(f"  [{'OK' if ok else 'FALTA'}] {label}")
