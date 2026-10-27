from pathlib import Path

c_path = Path(r"C:\AsuraPS3\ps3recomp\libs\spurs\cellSpurs.c")
c_txt = c_path.read_text(encoding="utf-8")

# Reemplazar desde typedef struct { uint32_t queue_ea; hasta el final del archivo con el descompresor HLE nativo
idx = c_txt.find("typedef struct {\n    uint32_t queue_ea;")
assert idx != -1, "No se encontro el bloque anterior en cellSpurs.c"

hle_zlib_code = r'''typedef struct {
    uint32_t queue_ea;
    uint8_t  data[32];
} AsuraLFQItem;

void asura_spu_lfq_pop(uint32_t queue_ea, uint8_t* dst32)
{
    (void)queue_ea; (void)dst32;
    /* HLE handles decompression synchronously in _cellSpursLFQueuePushBody; park SPU worker */
    for (;;) Sleep(10000);
}

/* --- RFC 1951 (Raw Deflate) + RFC 1950 (Zlib) Native HLE Decompressor --- */
typedef struct {
    const uint8_t* src;
    size_t src_len, src_pos;
    uint8_t* dst;
    size_t dst_cap, dst_pos;
    uint32_t bitbuf;
    int bitcnt;
} AsuraInflateState;

typedef struct {
    uint16_t count[16];
    uint16_t symbol[288];
} AsuraHuff;

static inline uint32_t asura_bits(AsuraInflateState* s, int need)
{
    uint32_t val = s->bitbuf;
    while (s->bitcnt < need) {
        uint8_t b = (s->src_pos < s->src_len) ? s->src[s->src_pos++] : 0;
        val |= (uint32_t)b << s->bitcnt;
        s->bitcnt += 8;
    }
    s->bitbuf = val >> need;
    s->bitcnt -= need;
    return val & ((1u << need) - 1u);
}

static int asura_huff_build(AsuraHuff* h, const uint8_t* lengths, int n)
{
    uint16_t offs[16];
    for (int i = 0; i < 16; i++) h->count[i] = 0;
    for (int i = 0; i < n; i++) h->count[lengths[i]]++;
    if (h->count[0] == n) return 0;
    offs[1] = 0;
    for (int i = 1; i < 15; i++) offs[i + 1] = offs[i] + h->count[i];
    for (int i = 0; i < n; i++)
        if (lengths[i]) h->symbol[offs[lengths[i]]++] = (uint16_t)i;
    return 0;
}

static inline int asura_huff_decode(AsuraInflateState* s, const AsuraHuff* h)
{
    int code = 0, first = 0, index = 0;
    for (int len = 1; len <= 15; len++) {
        code |= (int)asura_bits(s, 1);
        int count = h->count[len];
        if (code - count < first) return h->symbol[index + (code - first)];
        index += count;
        first += count;
        first <<= 1;
        code <<= 1;
    }
    return -1;
}

static int asura_inflate_raw(const uint8_t* src, size_t src_len, uint8_t* dst, size_t dst_cap, size_t* out_len)
{
    static const uint16_t lbase[29] = {
        3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,131,163,195,227,258
    };
    static const uint8_t lext[29] = {
        0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0
    };
    static const uint16_t dbase[30] = {
        1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577
    };
    static const uint8_t dext[30] = {
        0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13
    };
    static const uint8_t clorder[19] = {
        16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15
    };

    AsuraInflateState st = { src, src_len, 0, dst, dst_cap, 0, 0, 0 };
    uint32_t bfinal = 0;
    do {
        bfinal = asura_bits(&st, 1);
        uint32_t btype = asura_bits(&st, 2);
        if (btype == 0) {
            st.bitbuf = 0; st.bitcnt = 0;
            if (st.src_pos + 4 > st.src_len) return -1;
            uint16_t len  = (uint16_t)st.src[st.src_pos] | ((uint16_t)st.src[st.src_pos + 1] << 8);
            uint16_t nlen = (uint16_t)st.src[st.src_pos + 2] | ((uint16_t)st.src[st.src_pos + 3] << 8);
            st.src_pos += 4;
            if ((uint16_t)~nlen != len || st.src_pos + len > st.src_len || st.dst_pos + len > st.dst_cap) return -2;
            memcpy(st.dst + st.dst_pos, st.src + st.src_pos, len);
            st.src_pos += len; st.dst_pos += len;
        } else if (btype == 1 || btype == 2) {
            AsuraHuff ltree, dtree;
            uint8_t lengths[320];
            if (btype == 1) {
                for (int i = 0; i < 144; i++) lengths[i] = 8;
                for (int i = 144; i < 256; i++) lengths[i] = 9;
                for (int i = 256; i < 280; i++) lengths[i] = 7;
                for (int i = 280; i < 288; i++) lengths[i] = 8;
                asura_huff_build(&ltree, lengths, 288);
                for (int i = 0; i < 30; i++) lengths[i] = 5;
                asura_huff_build(&dtree, lengths, 30);
            } else {
                int hlit  = (int)asura_bits(&st, 5) + 257;
                int hdist = (int)asura_bits(&st, 5) + 1;
                int hclen = (int)asura_bits(&st, 4) + 4;
                for (int i = 0; i < 19; i++) lengths[i] = 0;
                for (int i = 0; i < hclen; i++) lengths[clorder[i]] = (uint8_t)asura_bits(&st, 3);
                asura_huff_build(&ltree, lengths, 19);
                int idx = 0;
                while (idx < hlit + hdist) {
                    int sym = asura_huff_decode(&st, &ltree);
                    if (sym < 0) return -3;
                    if (sym < 16) {
                        lengths[idx++] = (uint8_t)sym;
                    } else {
                        uint8_t rep_val = 0;
                        int rep_cnt = 0;
                        if (sym == 16) {
                            if (idx == 0) return -4;
                            rep_val = lengths[idx - 1];
                            rep_cnt = 3 + (int)asura_bits(&st, 2);
                        } else if (sym == 17) {
                            rep_cnt = 3 + (int)asura_bits(&st, 3);
                        } else {
                            rep_cnt = 11 + (int)asura_bits(&st, 7);
                        }
                        if (idx + rep_cnt > hlit + hdist) return -5;
                        while (rep_cnt--) lengths[idx++] = rep_val;
                    }
                }
                asura_huff_build(&ltree, lengths, hlit);
                asura_huff_build(&dtree, lengths + hlit, hdist);
            }
            for (;;) {
                int sym = asura_huff_decode(&st, &ltree);
                if (sym < 0) return -6;
                if (sym < 256) {
                    if (st.dst_pos >= st.dst_cap) return -7;
                    st.dst[st.dst_pos++] = (uint8_t)sym;
                } else if (sym == 256) {
                    break;
                } else {
                    sym -= 257;
                    if (sym >= 29) return -8;
                    int len = (int)lbase[sym] + (int)asura_bits(&st, lext[sym]);
                    int dsym = asura_huff_decode(&st, &dtree);
                    if (dsym < 0 || dsym >= 30) return -9;
                    size_t dist = (size_t)dbase[dsym] + (size_t)asura_bits(&st, dext[dsym]);
                    if (dist > st.dst_pos || st.dst_pos + (size_t)len > st.dst_cap) return -10;
                    for (int k = 0; k < len; k++) {
                        st.dst[st.dst_pos] = st.dst[st.dst_pos - dist];
                        st.dst_pos++;
                    }
                }
            }
        } else {
            return -11;
        }
    } while (!bfinal);
    if (out_len) *out_len = st.dst_pos;
    return 0;
}

s32 _cellSpursLFQueuePushBody(u64 queue_ea, u64 data_ea, u32 isBlocking)
{
    (void)isBlocking;
    if (!queue_ea || !data_ea) return CELL_SPURS_TASK_ERROR_NULL_POINTER;
    uint32_t q = (uint32_t)queue_ea;
    uint32_t d = (uint32_t)data_ea;

    uint32_t src_ea  = vm_read32(d + 0x00);
    uint32_t dst_ea  = vm_read32(d + 0x04);
    uint32_t src_sz  = vm_read32(d + 0x08);
    uint32_t dst_sz  = vm_read32(d + 0x0C);
    uint32_t status  = vm_read32(d + 0x10);
    uint32_t flag_ea = vm_read32(d + 0x14);
    uint16_t bits    = vm_read16(d + 0x18);
    uint16_t pre     = vm_read16(d + 0x1A);
    uint16_t post    = vm_read16(d + 0x1C);

    uint32_t total_out = (uint32_t)pre + dst_sz + (uint32_t)post;
    uint32_t status_ea = status & ~1u;
    int is_compressed  = (int)(status & 1u);

    int rc = 0;
    size_t got_out = 0;
    if (!is_compressed) {
        memcpy(vm_base + dst_ea, vm_base + src_ea + pre, dst_sz);
        got_out = dst_sz;
    } else {
        uint8_t* tmp = (pre == 0 && post == 0) ? (vm_base + dst_ea) : (uint8_t*)malloc(total_out);
        if (!tmp) return CELL_SPURS_TASK_ERROR_NOMEM;
        rc = asura_inflate_raw(vm_base + src_ea, src_sz, tmp, total_out, &got_out);
        if ((rc != 0 || got_out != total_out) && src_sz >= 6 &&
            (vm_base[src_ea] & 0x0F) == 8 && (((vm_base[src_ea] << 8) | vm_base[src_ea + 1]) % 31) == 0) {
            rc = asura_inflate_raw(vm_base + src_ea + 2, src_sz - 2, tmp, total_out, &got_out);
        }
        if (tmp != (vm_base + dst_ea)) {
            if (rc == 0) memcpy(vm_base + dst_ea, tmp + pre, dst_sz);
            free(tmp);
        }
    }

    static int _n = 0;
    if (_n < 40 || (_n % 250) == 0 || rc != 0) {
        fprintf(stderr, "[LFQPush#%d] q=0x%08X src=0x%08X(0x%X) -> dst=0x%08X(0x%X) status=0x%08X flag=0x%08X bits=0x%04X pre=%u post=%u => rc=%d got=0x%zX\n",
                _n, q, src_ea, src_sz, dst_ea, dst_sz, status, flag_ea, bits, pre, post, rc, got_out);
        fflush(stderr);
    }
    _n++;

    int should_signal = 1;
    if (status_ea != 0) {
        uint32_t old_val = vm_read32(status_ea);
        if (rc != 0) {
            vm_write32(status_ea, old_val | 0x80000000u);
            should_signal = 1;
        } else {
            uint32_t new_val = (old_val & 0x80000000u) | (((old_val & 0x7FFFFFFFu) - 1u) & 0x7FFFFFFFu);
            vm_write32(status_ea, new_val);
            should_signal = ((old_val & 0x7FFFFFFFu) == 1u);
        }
    }

    if (should_signal && flag_ea != 0) {
        cellSpursEventFlagSet((CellSpursEventFlag*)(uintptr_t)flag_ea, bits);
    }
    return CELL_OK;
}
'''

c_txt = c_txt[:idx] + hle_zlib_code
c_path.write_text(c_txt, encoding="utf-8")
print("[patch] Descompresor HLE Zlib/Deflate integrado en _cellSpursLFQueuePushBody!")
