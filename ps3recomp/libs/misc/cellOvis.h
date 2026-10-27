#ifndef PS3RECOMP_CELL_OVIS_H
#define PS3RECOMP_CELL_OVIS_H

#include "../../include/ps3emu/ps3types.h"
#include "../../include/ps3emu/error_codes.h"

#ifdef __cplusplus
extern "C" {
#endif

#define CELL_OVIS_ERROR_NOT_INITIALIZED     0x80410401
#define CELL_OVIS_ERROR_NO_OVERLAY          0x80410402
#define CELL_OVIS_ERROR_INVALID_ARGUMENT    0x80410403
#define CELL_OVIS_ERROR_ALREADY_INITIALIZED 0x80410404

typedef u32 CellOvisHandle;

s32 cellOvisInit(void);
s32 cellOvisTerm(void);
s32 cellOvisGetOverlayTableSize(const char* elf);
s32 cellOvisInitializeOverlayTable(void* ea_ovl_table, const char* elf);
s32 cellOvisFixSpursTasksetIfNecessary(void* taskset, void* ea_ovl_table);
s32 cellOvisCreateOverlay(const void* table, u32 tableSize, CellOvisHandle* handle);
s32 cellOvisDestroyOverlay(CellOvisHandle handle);
s32 cellOvisInvalidateOverlay(CellOvisHandle handle);

#ifdef __cplusplus
}
#endif

#endif /* PS3RECOMP_CELL_OVIS_H */
