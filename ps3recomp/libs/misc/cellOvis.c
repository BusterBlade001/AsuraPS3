/*
 * ps3recomp - cellOvis HLE implementation (Fixed for real PS3 SDK ABI)
 */
#include "cellOvis.h"
#include <stdio.h>
#include "../../runtime/ppu/ppu_memory.h"

static u32 s_next_handle = 1;

s32 cellOvisInit(void)
{
    return CELL_OK;
}

s32 cellOvisTerm(void)
{
    return CELL_OK;
}

/* Real PS3 SDK signature: int cellOvisGetOverlayTableSize(const char *elf)
 * Returns the overlay table size (>= 0) directly in r3, or 0 if no overlays. */
s32 cellOvisGetOverlayTableSize(const char* elf)
{
    (void)elf;
    return 0;
}

/* Real PS3 SDK signature: int cellOvisInitializeOverlayTable(void *ea_ovl_table, const char *elf) */
s32 cellOvisInitializeOverlayTable(void* ea_ovl_table, const char* elf)
{
    (void)ea_ovl_table;
    (void)elf;
    return CELL_OK;
}

s32 cellOvisFixSpursTasksetIfNecessary(void* taskset, void* ea_ovl_table)
{
    (void)taskset;
    (void)ea_ovl_table;
    return CELL_OK;
}

s32 cellOvisCreateOverlay(const void* table, u32 tableSize, CellOvisHandle* handle)
{
    (void)table; (void)tableSize;
    if (handle) vm_write32((u32)(uintptr_t)handle, (u32)s_next_handle++);
    return CELL_OK;
}

s32 cellOvisDestroyOverlay(CellOvisHandle handle)
{
    (void)handle;
    return CELL_OK;
}

s32 cellOvisInvalidateOverlay(CellOvisHandle handle)
{
    (void)handle;
    return CELL_OK;
}
