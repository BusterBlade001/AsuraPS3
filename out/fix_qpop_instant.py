from pathlib import Path
import re

sp_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
sp_txt = sp_path.read_text(encoding="latin-1")

# Reemplazar cellSpursQueuePopBody completo con la version instantanea para isBlocking=0 (AGAIN) e isBlocking=1 (CELL_OK + zero buffer)
pattern = r"s32 cellSpursQueuePopBody\(u64 queue_ea, u64 buffer_ea, u32 isPeek, u32 isBlocking\)\n\{.*?\n\}"
new_qpop_fn = """s32 cellSpursQueuePopBody(u64 queue_ea, u64 buffer_ea, u32 isPeek, u32 isBlocking)
{
    if (!queue_ea || !buffer_ea) return CELL_SPURS_TASK_ERROR_NULL_POINTER;
    u32 q   = (u32)queue_ea;
    u32 dst = (u32)buffer_ea;

    u32 head = vm_read32(q + 0x00);
    u32 tail = vm_read32(q + 0x04);
    u32 dep  = vm_read32(q + 0x0C);
    u32 sz   = vm_read32(q + 0x10);
    u32 buf  = (u32)vm_read64(q + 0x18);

    if (head == tail || dep == 0 || sz == 0 || buf == 0) {
        if (!isBlocking) {
            return (s32)0x80410901; /* CELL_SPURS_TASK_ERROR_AGAIN */
        }
        /* Synchronous pop (func_00891AE0): zero the 16B result struct (status=0) and return CELL_OK */
        memset(vm_base + dst, 0, sz ? sz : 16);
        return CELL_OK;
    }

    u32 slot = head % dep;
    memcpy(vm_base + dst, vm_base + buf + slot * sz, sz);
    if (!isPeek) {
        u32 nxt = (head + 1 < dep) ? head + 1 : 0;
        vm_write32(q + 0x00, nxt);
    }
    return CELL_OK;
}"""

assert re.search(pattern, sp_txt, flags=re.DOTALL), "No se encontro cellSpursQueuePopBody"
sp_txt = re.sub(pattern, new_qpop_fn, sp_txt, count=1, flags=re.DOTALL)
sp_path.write_text(sp_txt, encoding="latin-1")
print("[patch] cellSpursQueuePopBody actualizado (instantaneo sin bloqueo de 2s)!")
