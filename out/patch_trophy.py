from pathlib import Path

p = Path(r"C:\AsuraPS3\ps3recomp\libs\network\sceNpTrophy.c")
txt = p.read_text(encoding="utf-8")

# Ajustar total_trophies a 32 para que coincida con GetGameInfo
txt = txt.replace(
    "s_contexts[i].total_trophies = SCE_NP_TROPHY_MAX_NUM_TROPHIES;",
    "s_contexts[i].total_trophies = 32;"
)

old_info = '''    details = GUEST_PTR(details, SceNpTrophyGameDetails*);
    data = GUEST_PTR(data, SceNpTrophyGameData*);

    if (details) {
        memset(details, 0, sizeof(SceNpTrophyGameDetails));
        details->numTrophies = 32; /* default trophy set */
        details->numPlatinum = 1;
        details->numGold     = 2;
        details->numSilver   = 8;
        details->numBronze   = 21;
        strncpy(details->title, "PS3 Game",
                SCE_NP_TROPHY_GAME_TITLE_MAX_SIZE - 1);
        strncpy(details->description, "Trophy set",
                SCE_NP_TROPHY_GAME_DESC_MAX_SIZE - 1);
    }

    if (data) {
        memset(data, 0, sizeof(SceNpTrophyGameData));
        data->unlockedTrophies = trophy_count_unlocked(&s_contexts[context]);
        /* Count by grade would require per-trophy grade data;
         * return conservative estimates */
        data->unlockedPlatinum = 0;
        data->unlockedGold     = 0;
        data->unlockedSilver   = 0;
        data->unlockedBronze   = data->unlockedTrophies;
    }'''

new_info = '''    u32 details_ea = GUEST_EA(details);
    u32 data_ea    = GUEST_EA(data);

    if (details_ea) {
        memset(vm_base + details_ea, 0, sizeof(SceNpTrophyGameDetails));
        vm_write32(details_ea + 0x00, 32); /* numTrophies (BE) */
        vm_write32(details_ea + 0x04, 1);  /* numPlatinum (BE) */
        vm_write32(details_ea + 0x08, 2);  /* numGold     (BE) */
        vm_write32(details_ea + 0x0C, 8);  /* numSilver   (BE) */
        vm_write32(details_ea + 0x10, 21); /* numBronze   (BE) */
        strncpy((char*)(vm_base + details_ea + 0x14), "Asura's Wrath",
                SCE_NP_TROPHY_GAME_TITLE_MAX_SIZE - 1);
        strncpy((char*)(vm_base + details_ea + 0x14 + SCE_NP_TROPHY_GAME_TITLE_MAX_SIZE), "Trophy set",
                SCE_NP_TROPHY_GAME_DESC_MAX_SIZE - 1);
    }

    if (data_ea) {
        u32 unlocked = trophy_count_unlocked(&s_contexts[context]);
        memset(vm_base + data_ea, 0, sizeof(SceNpTrophyGameData));
        vm_write32(data_ea + 0x00, unlocked);
        vm_write32(data_ea + 0x04, 0);
        vm_write32(data_ea + 0x08, 0);
        vm_write32(data_ea + 0x0C, 0);
        vm_write32(data_ea + 0x10, unlocked);
    }'''

old_tinfo = '''    details = GUEST_PTR(details, SceNpTrophyDetails*);
    data = GUEST_PTR(data, SceNpTrophyData*);

    if (details) {
        memset(details, 0, sizeof(SceNpTrophyDetails));
        details->trophyId = (u32)trophyId;
        details->trophyGrade = SCE_NP_TROPHY_GRADE_BRONZE;
        snprintf(details->name, SCE_NP_TROPHY_NAME_MAX_SIZE,
                 "Trophy %d", trophyId);
        snprintf(details->description, SCE_NP_TROPHY_DESC_MAX_SIZE,
                 "Trophy #%d description", trophyId);
        details->hidden = 0;
    }

    if (data) {
        memset(data, 0, sizeof(SceNpTrophyData));
        data->trophyId = (u32)trophyId;
        data->unlocked = s_contexts[context].unlocked[trophyId];
        data->timestamp = s_contexts[context].unlock_time[trophyId];
    }'''

new_tinfo = '''    u32 details_ea = GUEST_EA(details);
    u32 data_ea    = GUEST_EA(data);

    if (details_ea) {
        memset(vm_base + details_ea, 0, sizeof(SceNpTrophyDetails));
        vm_write32(details_ea + 0x00, (u32)trophyId);
        vm_write32(details_ea + 0x04, SCE_NP_TROPHY_GRADE_BRONZE);
        snprintf((char*)(vm_base + details_ea + 0x08), SCE_NP_TROPHY_NAME_MAX_SIZE,
                 "Trophy %d", trophyId);
        snprintf((char*)(vm_base + details_ea + 0x08 + SCE_NP_TROPHY_NAME_MAX_SIZE), SCE_NP_TROPHY_DESC_MAX_SIZE,
                 "Trophy #%d description", trophyId);
    }

    if (data_ea) {
        memset(vm_base + data_ea, 0, sizeof(SceNpTrophyData));
        vm_write64(data_ea + 0x00, s_contexts[context].unlock_time[trophyId]);
        vm_write32(data_ea + 0x08, (u32)trophyId);
        *(vm_base + data_ea + 0x0C) = s_contexts[context].unlocked[trophyId];
    }'''

assert old_info in txt, "old_info not found"
assert old_tinfo in txt, "old_tinfo not found"
txt = txt.replace(old_info, new_info, 1).replace(old_tinfo, new_tinfo, 1)
p.write_text(txt, encoding="utf-8")
print("[patch] sceNpTrophy.c corregido a Big-Endian!")
