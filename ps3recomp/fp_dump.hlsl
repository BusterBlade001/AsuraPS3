/* fp_addr=0x0DCED881 vmoff=0xCDCED880 raw: 82 00 17 04 C8 01 1C 9D C8 00 00 01 C8 00 3F E1 10 02 01 00 00 02 1C 9C C8 00 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc0).xyzw).xy)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4(1,0,0,0)).xxxx); r[1].w = _v.w; }
    { float4 _v = (float4)((r[0]).xxxx); r[1].z = _v.z; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((input.tc0).xyzw).xy)); r[0].x = _v.x; }
    { float4 _v = (float4)((r[0]).xxxx); r[1].y = _v.y; }
    { float4 _v = (float4)((float4(1,0,0,0)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).xyzw).xy)); r[1].x = _v.x; }
    { float4 _v = (float4)(dot(((r[1]).xyzw), ((float4(1.16412,-0.813477,-0.391449,0.529705)).xyzw))); r[0].y = _v.y; }
    { float4 _v = (float4)(dot(((r[1]).xzwx).xyz, ((float4(1.16412,2.01782,-1.08167,0)).xyzw).xyz)); r[0].z = _v.z; }
    { float4 _v = (float4)(dot(((r[1]).xywz).xyz, ((float4(1.16412,1.59579,-0.870655,0)).xyzw).xyz)); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(1,0,0,0)).xxxx)); r[0].xyz = _v.xyz; }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00000001 vmoff=0xC0000000 raw: 1E 7E 7E 00 C8 00 1C 9D C8 00 00 01 C8 00 00 01 1E 01 01 00 00 02 1C 9C C8 00 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx); r[0].xyzw = _v.xyzw; }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00000041 vmoff=0xC0000040 raw: 1E 7E 7E 00 C8 00 1C 9D C8 00 00 01 C8 00 00 01 1E 01 01 00 C8 02 1C 9D C8 00 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)((float4(0,0,0,1)).xyzw); r[0].xyzw = _v.xyzw; }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00000081 vmoff=0xC0000080 raw: 22 00 01 01 FE 01 1C 9D C8 00 00 01 C8 00 3F E1 02 00 3A 00 00 02 1C 9E C8 00 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)((input.tc5).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[0]).xyzw) + (-((float4(-9.99,0.999,-0.1001,-0.1)).yyyy))); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[0]).xxxx) + ((float4(0,0,0,1)).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0,0,0,1)).xyzw); r[0].xyz = _v.xyz; }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00000141 vmoff=0xC0000140 raw: 22 00 01 01 FE 01 1C 9D C8 00 00 01 C8 00 3F E1 02 00 3A 00 00 02 1C 9E C8 00 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)((input.tc5).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[0]).xyzw) + (-((float4(-9.99,0.999,-0.1001,-0.1)).yyyy))); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[0]).xxxx) + ((float4(0,0,0,1)).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0,0,0,1)).xyzw); r[0].xyz = _v.xyz; }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00000201 vmoff=0xC0000200 raw: 1E 7E 7E 00 C8 00 1C 9D C8 00 00 01 C8 00 00 01 1E 01 01 00 00 02 1C 9C C8 00 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx); r[0].xyzw = _v.xyzw; }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00000241 vmoff=0xC0000240 raw: 08 04 01 00 00 02 1C 9C C8 00 00 01 C8 00 00 01 00 00 3F 80 00 00 00 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
    float4 t2 : SV_TARGET2;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)((float4(1,0,0,0)).xxxx); r[2].z = _v.z; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc0).wzzz).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((r[0]).yyyy));
      cc0.x = _v.x;
    }
    { float4 _v = (float4)((float4(1,0,0,0)).xxxx); r[2].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[1].SampleLevel(rsx_samp[1], ((input.tc1).wzzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].z = _v.z; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc0).xyzw).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(((r[1]).xxxx) + ((r[1]).xyzw));
      cc0.y = _v.y;
    }
    { float4 _v = (float4)(rsx_tex[1].SampleLevel(rsx_samp[1], ((input.tc1).xyzw).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).zzzz) + ((float4(-1,0,0,0)).xxxx)); r[2].x = _v.x; }
    { float4 _v = (float4)((float4(0,1,0,0)).yyyy); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[1].x = _v.x; }
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].z = (_p.z != 0.0) ? _v.z : r[0].z;
    }
    { float4 _v = (float4)(((r[1]).xxxx) + ((float4(-1,0,0,0)).xxxx)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0,1,0,0)).yyyy); r[1].x = _v.x; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).wwww).x); r[1].z = _v.z; }
    { float4 _v = (float4)((float4(0,0,0,0)).yyyy);
      float4 _p = (float4)((cc0).yyyy <= (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(((r[1]).xyzw) + ((r[0]).zzzz)); r[3].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).xyzw).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((r[0]).yyyy));
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).wzzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].w = (_p.w != 0.0) ? _v.w : r[2].w;
    }
    { float4 _v = (float4)(((r[1]).xyzw) + ((r[1]).yyyy));
      cc0.x = _v.x;
    }
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].z = (_p.z != 0.0) ? _v.z : r[2].z;
    }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[3]).xxxx) + ((r[2]).xyzw)); r[2].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[1].SampleLevel(rsx_samp[1], ((input.tc0).wzzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(1,0,0,0)).xxxx); r[3].x = _v.x; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[2]).xyzw).x); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(0,-1,0,0)).yyyy)); r[2].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[1].SampleLevel(rsx_samp[1], ((input.tc0).xyzw).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[2].y = _v.y; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[2]).xyzw).x); r[1].y = _v.y; }
    { float4 _v = (float4)(((r[2]).wwww) + ((r[2]).zzzz)); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[2]).yyyy) + ((float4(-1,0,0,0)).xxxx)); r[2].w = _v.w; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[2]).wwww).x); r[1].x = _v.x; }
    { float4 _v = (float4)(dot(((r[1]).xyzw), ((float4(0.25,0,0,0)).xxxx))); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[1]).xyzw) + (-((r[0]).wwww))); r[1].y = _v.y; }
    { float4 _v = (float4)(((r[1]).xxxx) + (-((r[0]).xyzw))); r[2].w = _v.w; }
    { float4 _v = (float4)((float4)((abs((r[1]).yyyy)) <  (abs((r[2]).wwww))));
      cc0.x = _v.x;
    }
    { float4 _v = (float4)((r[2]).wwww); r[1].x = _v.x; }
    { float4 _v = (float4)((r[1]).yyyy);
      float4 _p = (float4)((cc0).xxxx != (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(((r[1]).zzzz) + (-((r[0]).wwww))); r[1].y = _v.y; }
    { float4 _v = (float4)((r[1]).xxxx); r[3].w = _v.w; }
    { float4 _v = (float4)((float4)((abs((r[1]).yyyy)) <  (abs((r[1]).xyzw))));
      cc0.x = _v.x;
    }
    { float4 _v = (float4)((r[1]).yyyy);
      float4 _p = (float4)((cc0).xxxx != (float4)0.0);
      r[3].w = (_p.w != 0.0) ? _v.w : r[3].w;
    }
    { float4 _v = (float4)(((r[1]).wwww) + (-((r[0]).wwww))); r[3].y = _v.y; }
    { float4 _v = (float4)((r[3]).xyzw); r[1].w = _v.w; }
    { float4 _v = (float4)((float4)(((r[2]).xyzw) >  ((float4(1,0,0,0)).xxxx)));
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).xyzw).xy)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)((float4)((abs((r[3]).yyyy)) <  (abs((r[3]).xyzw))));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)((float4(-1,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).xxxx == (float4)0.0);
      r[3].x = (_p.x != 0.0) ? _v.x : r[3].x;
    }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).wzzz).xy)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((r[1]).xyzw)); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)((r[3]).yyyy);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      r[1].w = (_p.w != 0.0) ? _v.w : r[1].w;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[1]).xyzw) + ((r[0]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)(((h[2]).xyzw) + ((r[2]).xyzw)); h[7].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).wzzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(65503,0,0,0)).xxxx))); r[0].w = _v.w; }
    { float4 _v = (float4)(((h[7]).xyzw) + ((r[0]).xyzw)) / 4.0; r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[3]).xxxx)); r[0].w = _v.w; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    float4 _o2 = r[3];
    _out.t2 = (_o2 == _o2) ? _o2 : (float4)0;
    return _out;
}

/* fp_addr=0x00000801 vmoff=0xC0000800 raw: 98 00 03 00 80 01 1C 9C 80 02 00 00 C8 00 3F E1 00 00 BB 00 00 00 BD 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(((input.tc0).xxxy) + ((float4(-0.00195312,-0.03125,0,0)).xxxy)); r[0].zw = _v.zw; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((float4(16,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)((r[0]).wwww); r[0].y = _v.y; }
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)(frac((r[0]).xyzw)); r[0].x = _v.x; }
    { float4 _v = (float4)((-((r[0]).xxxx)) * ((float4(0.0625,0,0,0)).xxxx) + ((r[0]).xyzw)); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(1.06667,0,0,0)).xxxx)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(1,0,0,1)).xxxx)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) + (-((float4(0,0,0,1)).xyzw))); _v = saturate(_v); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0,0,0,1e-08)).xyzw))); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(1,1,1,0)).xyzw)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(max(((r[0]).yyyy), ((float4(1e-08,0,0,0)).xxxx))); r[1].x = _v.x; }
    { float4 _v = (float4)(log2(((r[0]).wwww).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(1e-08,0,0,0)).xxxx))); r[0].z = _v.z; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(1e-08,0,0,0)).xxxx))); r[0].x = _v.x; }
    { float4 _v = (float4)(log2(((r[1]).xyzw).x)); r[0].y = _v.y; }
    { float4 _v = (float4)((float4(1,1,1,0.454545)).xyzw); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(log2(((r[0]).zzzz).x)); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(1,1,1,1)).yyyy)); r[0].y = _v.y; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(1,1,1,1)).xyzw)); r[0].z = _v.z; }
    { float4 _v = (float4)(log2(((r[0]).xyzw).x)); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(1,1,1,1)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)(exp2(((r[0]).xyzw).x)); r[0].x = _v.x; }
    { float4 _v = (float4)(exp2(((r[0]).yyyy).x)); r[0].y = _v.y; }
    { float4 _v = (float4)(exp2(((r[0]).zzzz).x)); r[0].z = _v.z; }
    { float4 _v = (float4)(dot(((r[0]).xyzw).xyz, ((float4(0,0,0,0)).xyzw).xyz)); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(0,0,0,1)).wwww) + ((r[2]).xxxx)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[1]).xyzw) + ((float4(0,0,0,0)).xyzw)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(1,1,1,1)).xyzw)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(1e-08,0,0,0)).xxxx))); r[0].z = _v.z; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(1e-08,0,0,0)).xxxx))); r[0].y = _v.y; }
    { float4 _v = (float4)(log2(((r[0]).yyyy).x)); r[0].y = _v.y; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(1e-08,0,0,0)).xxxx))); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[1]).wwww) * ((float4(2.2,0,0,0)).xxxx)); r[1].x = _v.x; }
    { float4 _v = (float4)(log2(((r[0]).zzzz).x)); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[1]).xxxx) * ((r[0]).xyzw)); r[0].y = _v.y; }
    { float4 _v = (float4)(log2(((r[0]).xyzw).x)); r[1].y = _v.y; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).wwww)); r[0].x = _v.x; }
    { float4 _v = (float4)(exp2(((r[0]).xyzw).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[1]).yyyy) * ((r[1]).xyzw)); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).zzzz)); r[1].x = _v.x; }
    { float4 _v = (float4)(exp2(((r[0]).xyzw).x)); r[0].x = _v.x; }
    { float4 _v = (float4)(exp2(((r[0]).yyyy).x)); r[0].y = _v.y; }
    { float4 _v = (float4)(exp2(((r[1]).xyzw).x)); r[0].z = _v.z; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    return _out;
}

/* fp_addr=0x00000C41 vmoff=0xC0000C40 raw: BE 02 17 00 C8 01 1C 9D C8 00 00 01 C8 00 3F E1 0E 82 01 00 C8 04 1C 9D C8 00 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).xyzw).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)((r[1]).xyzw); h[1].xyz = _v.xyz; }
    { float4 _v = (float4)(abs((r[1]).xyzw)); h[1].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).xyzw).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)((r[1]).xyzw); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(abs((r[1]).xyzw)); h[0].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).wzzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)((r[1]).xyzw); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)(abs((r[1]).xyzw)); h[2].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) + ((h[2]).xyzw)); h[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((h[0]).xyzw) + ((h[1]).xyzw)); h[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).wzzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)((r[1]).xyzw); h[1].xyz = _v.xyz; }
    { float4 _v = (float4)(abs((r[1]).xyzw)); h[1].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) + ((h[1]).xyzw)) / 4.0; h[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((float4(0,0.0005,4,0)).xxxx))); h[1].w = _v.w; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).yyyy); h[1].x = _v.x; }
    { float4 _v = (float4)((float4)(((h[0]).wwww) <  ((float4(0,0.0005,4,0)).xxxx)));
      cc0.x = _v.x;
    }
    { float4 _v = (float4)((abs((h[1]).xyzw)) * ((float4(0,0.0005,4,0)).yyyy)); _v = saturate(_v); h[0].w = _v.w; }
    { float4 _v = (float4)(log2(((h[0]).wwww).x)); h[0].w = _v.w; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).xxxx);
      float4 _p = (float4)((cc0).xxxx != (float4)0.0);
      h[1].x = (_p.x != 0.0) ? _v.x : h[1].x;
    }
    { float4 _v = (float4)(((h[0]).xyzw) * ((float4(0,0.0005,4,0)).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].w = _v.w; }
    { float4 _v = (float4)(min(((h[1]).xxxx), ((h[0]).xyzw))); h[0].w = _v.w; }
    { float4 _v = (float4)(max(((h[0]).xyzw), ((float4(0,0.0005,4,0)).xyzw))); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[0]).wwww)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) * ((float4(0.25,0,0,0)).xxxx)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) != ((r[0]).xyzw)));
      cc0.xyzw = _v.xyzw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).xyzw != (float4)0.0);
      r[0].xyzw = (_p.xyzw != 0.0) ? _v.xyzw : r[0].xyzw;
    }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00000EC1 vmoff=0xC0000EC0 raw: 9E 02 01 00 C8 01 1C 9D C8 00 00 01 C8 00 3F E1 1E 80 0D 00 68 04 1C 9D 88 02 00 00 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)((input.tc0).xyzw); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4)(((r[1]).xywz) >  ((float4(0,0,0.999219,0.998611)).xyxy))); h[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)((input.tc2).xyzw); r[2].xy = _v.xy; }
    { float4 _v = (float4)((float4)(((r[1]).xywz) <  ((float4(0,0,0.999219,0.998611)).zwzw))); h[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)((input.tc1).xyzw); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[1]).xyzw)); h[5].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4)(((r[1]).xywz) >  ((float4(0,0,0.999219,0.998611)).xyxy))); h[6].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4)(((r[1]).xywz) <  ((float4(0,0,0.999219,0.998611)).zwzw))); h[7].xyzw = _v.xyzw; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).wzzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((h[6]).zwxy) * ((h[7]).zwxy)); h[6].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4)(((r[2]).xxxy) <  ((float4(0,0,0.999219,0.998611)).xyzw))); h[2].zw = _v.zw; }
    { float4 _v = (float4)((float4)(((r[2]).xyzw) >  ((float4(0,0,0.999219,0.998611)).xyxx))); h[2].xy = _v.xy; }
    { float4 _v = (float4)(((h[2]).xxxy) * ((h[2]).xyzw)); h[7].zw = _v.zw; }
    { float4 _v = (float4)(((h[5]).xzzw) * ((h[5]).ywzw)); h[7].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).xyzw).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((h[7]).xxxx)); r[2].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((h[7]).yyyy) * ((r[0]).xyzw)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((h[6]).zxzw) * ((h[6]).wyzw)); h[6].xy = _v.xy; }
    { float4 _v = (float4)(((h[7]).zzzz) * ((h[7]).xyzw)); h[6].w = _v.w; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((float4(0.304005,0.304005,0.304005,0.304005)).xyzw)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((float4(0.0939128,0.0939128,0.0939128,0.0939128)).xyzw) + ((r[1]).xyzw)); r[2].xyzw = _v.xyzw; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).wzzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((h[6]).yyyy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).xyzw).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((h[6]).xxxx)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)((r[2]).xyzw); r[2].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(0.384337,0.384337,0.384337,0.384337)).xyzw) + ((r[2]).xyzw)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((float4(0.190114,0.190114,0.190114,0.190114)).xyzw) + ((r[0]).xyzw)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc2).xyzw).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((h[6]).wwww)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(0.0276305,0.0276305,0.0276305,0.0276305)).xyzw) + ((r[1]).xyzw)); r[0].xyzw = _v.xyzw; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    return _out;
}

/* fp_addr=0x00001441 vmoff=0xC0001440 raw: B0 00 2F 06 5C 01 1C 9D 00 02 00 00 C8 00 3F E1 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
    float4 t2 : SV_TARGET2;
    float4 t3 : SV_TARGET3;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[3].SampleLevel(rsx_samp[3], ((input.tc1).zwzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).zwzz).xy)); r[3].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((float4(-1,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[3]).xxxx) >  (-((r[3]).yyyy)))); h[0].z = _v.z; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz); r[2].x = _v.x; }
    { float4 _v = (float4)((r[0]).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) <  ((float4(14,0,0,0)).xxxx))); h[1].w = _v.w; }
    { float4 _v = (float4)((float4)(((h[0]).zzzz) == ((float4(0,0,0,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz);
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[1]).xyzw));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)((-((r[3]).wwww)) + ((float4(1,0,0,0)).xxxx)); r[2].y = _v.y; }
    { float4 _v = (float4)((float4(65504,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      r[0].x = (_p.x != 0.0) ? _v.x : r[0].x;
    }
    { float4 _v = (float4)((input.tc0).xxxy); r[0].zw = _v.zw; }
    { float4 _v = (float4)((h[0]).zzzz);
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[0]).xxxx)); r[3].z = _v.z; }
    { float4 _v = (float4)(((r[3]).zzzz) * ((float4(0,1,0,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((r[0]).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[1]).wwww) * ((float4(1,0,0,0)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xxxx) * ((float4(0,8.4771e-07,0.999,1)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + ((float4(0,-7.62939e-06,-9.99,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) / ((r[1]).zzzz).x); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].w = (_p.w != 0.0) ? _v.w : r[4].w;
    }
    { float4 _v = (float4)(((r[0]).zwzz) + (-((r[0]).xyzw))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[3]).xxxy) * ((float4(2,-1,0,0)).xxxx) + ((float4(2,-1,0,0)).yyyy)); h[1].zw = _v.zw; }
    { float4 _v = (float4)(((r[0]).xxxy) * ((float4(0,0,0,0)).xxxy));
      float4 _p = (float4)((cc0).wwww == (float4)0.0);
      h[1].zw = (_p.zw != 0.0) ? _v.zw : h[1].zw;
    }
    { float4 _v = (float4)((float4(0,0,0,0)).zzzz); h[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)) * 2.0; r[4].xy = _v.xy; }
    { float4 _v = (float4)(dot(((h[1]).zwzz).xy, ((h[1]).zwzz).xy)); h[1].x = _v.x; }
    { float4 _v = (float4)((float4)(((h[1]).xxxx) >  ((float4(1,0,0,0)).xxxx)));
      cc0.y = _v.y;
    }
    { float4 _v = (float4)((input.tc1).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)((h[1]).xyzw); h[0].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) + (-((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)));
      float4 _p = (float4)((cc0).xxxx > (float4)0.0);
      h[0].xy = (_p.xy != 0.0) ? _v.xy : h[0].xy;
    }
    { float4 _v = (float4)((abs((h[1]).xyzw) > 0.0 ? ((h[1]).xyzw) / sqrt(abs(((h[1]).xyzw).x)) : (float4)0.0));
      float4 _p = (float4)((cc0).yyyy != (float4)0.0);
      h[0].zw = (_p.zw != 0.0) ? _v.zw : h[0].zw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((h[0]).zwzz) * ((float4(0.0125,0.0222222,0.1,0.05625)).xyxx) + ((h[0]).xyzw)); r[4].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[4]).wwww) + ((r[1]).xyzw)); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx); r[1].x = _v.x; }
    { float4 _v = (float4)((float4(-0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(min(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[1]).xxxx) + ((r[1]).zwzz)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.6,0,0,1)).xxxx); r[2].w = _v.w; }
    { float4 _v = (float4)(min(((r[1]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[2].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].w = (_p.w != 0.0) ? _v.w : r[2].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[5].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[2]).xxxy), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((r[1]).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[2]).wwww) + ((r[1]).xyzw)); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[3].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((h[3]).xyzw).xy, ((h[3]).xyzw).xy)); r[2].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].w = (_p.w != 0.0) ? _v.w : r[1].w;
    }
    { float4 _v = (float4)((-((r[2]).xyzw)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].x = _v.x; }
    { float4 _v = (float4)(dot(((h[5]).xyzw).xy, ((h[5]).xyzw).xy)); r[1].x = _v.x; }
    { float4 _v = (float4)((-((r[1]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].w = _v.w; }
    { float4 _v = (float4)((r[2]).xyzw); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[0]).wwww)); r[5].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[1]).xyzw)); r[2].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).zwzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).wwww) + ((r[0]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)((float4)((abs((r[1]).xyzw)) <  ((float4(0,0.0005,4,0)).xxxx)));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(min(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[5].y = _v.y; }
    { float4 _v = (float4)(((r[0]).wwww) + ((r[2]).wwww)); h[11].x = _v.x; }
    { float4 _v = (float4)(max(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[5].y = (_p.y != 0.0) ? _v.y : r[5].y;
    }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).xxxx) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[5]).xxxx) + ((h[11]).xxxx)); h[9].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[3]).zwzz).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[0]).xxxy)); h[11].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[3]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((h[11]).zwzz).xy, ((h[11]).zwzz).xy)); r[5].x = _v.x; }
    { float4 _v = (float4)((-((r[5]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).yyyy)); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((input.tc0).zwzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[7].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).yyyy); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[2]).wwww) + ((h[9]).wwww)); h[5].z = _v.z; }
    { float4 _v = (float4)((abs((r[1]).xyzw)) + (-((float4(0,0.0005,4,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((abs((h[0]).wwww)) * ((float4(0,0.0005,4,0)).yyyy)); _v = saturate(_v); h[9].x = _v.x; }
    { float4 _v = (float4)(log2(((h[9]).xyzw).x)); h[9].x = _v.x; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      h[0].x = (_p.x != 0.0) ? _v.x : h[0].x;
    }
    { float4 _v = (float4)(((h[9]).xxxx) * ((float4(0,0.0005,4,0)).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].y = _v.y; }
    { float4 _v = (float4)(min(((h[0]).xyzw), ((h[0]).yyyy))); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((float4(80,45,0,0)).xxxy)); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((h[0]).xyzw), ((float4(0,0.0005,4,0)).wwww))); h[1].x = _v.x; }
    { float4 _v = (float4)((-((h[1]).xxxx)) + ((float4(0,1,0,0)).yyyy)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.8,0,0,1)).xxxx); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((h[7]).xyzw)); h[3].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((h[7]).xyzw)); h[3].w = _v.w; }
    { float4 _v = (float4)((input.tc1).zwzz); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(-0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].z = (_p.z != 0.0) ? _v.z : r[0].z;
    }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[0]).zzzz) + ((r[0]).xyzw)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyxx))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[0]).xyzw).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[1]).xxxy)); h[2].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[0]).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].x = (_p.x != 0.0) ? _v.x : r[4].x;
    }
    { float4 _v = (float4)(dot(((h[2]).zwzz).xy, ((h[2]).zwzz).xy)); r[4].y = _v.y; }
    { float4 _v = (float4)(((h[3]).xyzw) / ((h[3]).wwww).x); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)((-((r[4]).yyyy)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((r[4]).zwzz).xy, ((r[4]).zwzz).xy)); r[1].z = _v.z; }
    { float4 _v = (float4)(((r[1]).wwww) * ((r[4]).xyzw)); r[3].x = _v.x; }
    { float4 _v = (float4)((abs(abs((r[1]).zzzz)) > 0.0 ? (abs((r[1]).zzzz)) / sqrt(abs(((r[1]).zzzz).x)) : (float4)0.0)); _v = saturate(_v); h[5].w = _v.w; }
    { float4 _v = (float4)(((h[5]).xyzw) * ((r[0]).xyzw)); h[2].w = _v.w; }
    { float4 _v = (float4)((-((h[2]).xyzw)) * ((r[0]).xyzw) + ((r[0]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[3]).xxxx) + ((r[2]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[3]).xxxx) + ((h[5]).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) / ((h[0]).wwww).x); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((h[2]).xyzw))); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[2]).wwww) * ((h[0]).xyzw) + ((h[2]).xyzw)) / 4.0; r[0].xyz = _v.xyz; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    float4 _o2 = r[3];
    _out.t2 = (_o2 == _o2) ? _o2 : (float4)0;
    float4 _o3 = r[4];
    _out.t3 = (_o3 == _o3) ? _o3 : (float4)0;
    return _out;
}

/* fp_addr=0x00002041 vmoff=0xC0002040 raw: 8E 00 17 00 C8 01 1C 9D C8 00 00 01 C8 00 3F E1 0E 80 02 00 C8 00 1C 9D 00 02 00 00 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).wzzz).xy)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[1].xyz = _v.xyz; }
    { float4 _v = (float4)(max(((h[0]).yyyy), ((h[0]).zzzz))); h[0].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).xyzw).xy)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[4].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).wzzz).xy)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(max(((h[1]).yyyy), ((h[1]).zzzz))); h[1].w = _v.w; }
    { float4 _v = (float4)(max(((h[1]).xxxx), ((h[1]).xyzw))); h[3].w = _v.w; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[5].xyz = _v.xyz; }
    { float4 _v = (float4)(max(((h[4]).yyyy), ((h[4]).zzzz))); h[4].w = _v.w; }
    { float4 _v = (float4)(((h[3]).wwww) + (-((float4(1,1,0,0)).yyyy))) / 2.0; _v = saturate(_v); h[2].x = _v.x; }
    { float4 _v = (float4)(max(((h[5]).yyyy), ((h[5]).zzzz))); h[1].w = _v.w; }
    { float4 _v = (float4)((r[1]).xyzw); r[1].xy = _v.xy; }
    { float4 _v = (float4)(max(((h[0]).xxxx), ((h[0]).xyzw))); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[1]).xyzw) * ((h[2]).xxxx)); h[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).wwww) + (-((float4(1,1,0,0)).yyyy))) / 2.0; _v = saturate(_v); h[2].x = _v.x; }
    { float4 _v = (float4)(max(((h[4]).xxxx), ((h[4]).xyzw))); h[0].w = _v.w; }
    { float4 _v = (float4)(max(((h[5]).xxxx), ((h[1]).xyzw))); h[1].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[2]).xxxx) + ((h[1]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((float4(1,1,0,0)).yyyy))) / 2.0; _v = saturate(_v); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[4]).xyzw) * ((h[0]).wwww) + ((h[0]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[1]).xyzw) + (-((float4(1,1,0,0)).yyyy))) / 2.0; _v = saturate(_v); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[5]).xyzw) * ((h[0]).wwww) + ((h[0]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) * ((float4(1,1,0,0)).xxxx)) / 4.0; r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(0.25,0,0,0)).xxxx)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) != ((r[0]).xyzw)));
      cc0.xyzw = _v.xyzw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).xyzw != (float4)0.0);
      r[0].xyzw = (_p.xyzw != 0.0) ? _v.xyzw : r[0].xyzw;
    }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00002881 vmoff=0xC0002880 raw: A6 00 01 00 5C 01 1C 9D C8 00 00 01 C8 00 3F E1 06 00 08 00 C8 00 1C 9D 5C 02 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)((input.tc1).zwzz); r[0].xy = _v.xy; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.998438,0.997222)).zwzz))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.998438,0.997222)).xyxx))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((r[0]).xyzw).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].SampleLevel(rsx_samp[0], ((input.tc1).xyzw).xy, ((float4(0,0,0,0)).xxxx).x)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + (-((r[0]).xyzw))); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((r[0]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((h[0]).xyzw).xyz, ((float4(-0.900146,-1.76953,-0.329956,0)).xyzw).xyz)); h[0].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc0).zwzz).xy)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].w = _v.w; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((float4(1,1,1,10)).xyzw)) * 4.0; h[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) * ((float4(1,1,1,10)).xyzw)); _v = saturate(_v); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[1]).xyzw) * ((h[0]).wwww) + ((h[0]).xyzw)); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)(log2(((h[2]).xyzw).x)); r[0].x = _v.x; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(0.454545,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)(log2(((h[2]).zzzz).x)); r[0].z = _v.z; }
    { float4 _v = (float4)(log2(((h[2]).yyyy).x)); r[0].y = _v.y; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((float4(0.454545,0,0,0)).xxxx)); r[1].x = _v.x; }
    { float4 _v = (float4)(exp2(((r[1]).xyzw).x)); _v = saturate(_v); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).yyyy) * ((float4(0.454545,0,0,0)).xxxx)); r[1].x = _v.x; }
    { float4 _v = (float4)(((r[0]).wwww) * ((float4(14.9999,0,0,0)).xxxx)); r[0].y = _v.y; }
    { float4 _v = (float4)(floor((r[0]).xyzw)); r[1].y = _v.y; }
    { float4 _v = (float4)(exp2(((r[1]).xyzw).x)); _v = saturate(_v); r[1].x = _v.x; }
    { float4 _v = (float4)(((r[1]).yyyy) * ((float4(0.0625,0,0,0)).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[1]).xxxx) * ((float4(0,0.9375,0,0)).yyyy)); r[1].z = _v.z; }
    { float4 _v = (float4)(exp2(((r[0]).xyzw).x)); _v = saturate(_v); r[0].x = _v.x; }
    { float4 _v = (float4)((r[1]).zzzz); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xxxx) * ((float4(0.0585938,0,0,0)).xxxx) + ((r[1]).wwww)); r[2].z = _v.z; }
    { float4 _v = (float4)((-((r[1]).xyzw)) * ((float4(16,0,0,0)).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[2]).zwzz) + ((float4(0.00195312,0.03125,0,0)).xyxx)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[3].Sample(rsx_samp[3], ((r[0]).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((r[1]).zzzz); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[2]).xyzw) + ((float4(0.0625,0,0,0)).xxxx)); r[2].z = _v.z; }
    { float4 _v = (float4)(((r[2]).zwzz) + ((float4(0.00195312,0.03125,0,0)).xyxx)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[3].Sample(rsx_samp[3], ((r[1]).xyzw).xy)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + (-((r[0]).xyzw))); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(15,0,0,0)).xxxx) + ((r[1]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((r[0]).xyzw)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((r[0]).xyzw).xyz, ((float4(0.299,0.587,0.114,0)).xyzw).xyz)); r[0].w = _v.w; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    return _out;
}

/* fp_addr=0x00002C41 vmoff=0xC0002C40 raw: 9E 00 17 00 C8 01 1C 9D C8 00 00 01 C8 00 3F E1 0E 02 01 00 C8 00 1C 9D C8 00 00 01 C8 00 00 01 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
float4 main(PSInput input) : SV_TARGET {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc0).xyzw).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)((r[0]).xyzw); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((r[0]).xyzw), ((float4(0,0,0,1)).xyzw))); r[1].w = _v.w; }
    { float4 _v = (float4)((float4(0.454545,0.00138889,0.998438,0.997222)).xxxx); h[4].x = _v.x; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((input.tc1).xyzw)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4)(((h[4]).xyzw) != ((float4(1,0,0,0)).xxxx)));
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(log2(((r[0]).yyyy).x)); r[1].y = _v.y; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((float4(0.454545,0.00138889,0.998438,0.997222)).xxxx)); r[1].y = _v.y; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].w = _v.w; }
    { float4 _v = (float4)(log2(((r[0]).zzzz).x)); r[1].z = _v.z; }
    { float4 _v = (float4)(((r[1]).zzzz) * ((float4(0.454545,0.00138889,0.998438,0.997222)).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(log2(((r[0]).xyzw).x)); r[1].x = _v.x; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((float4(0.454545,0.00138889,0.998438,0.997222)).xxxx)); r[1].x = _v.x; }
    { float4 _v = (float4)(exp2(((r[1]).xyzw).x)); r[1].x = _v.x; }
    { float4 _v = (float4)(exp2(((r[1]).yyyy).x)); r[1].y = _v.y; }
    { float4 _v = (float4)(exp2(((r[1]).wwww).x)); r[1].z = _v.z; }
    { float4 _v = (float4)((r[1]).xyzw);
      float4 _p = (float4)((cc0).xxxx != (float4)0.0);
      r[0].xyz = (_p.xyz != 0.0) ? _v.xyz : r[0].xyz;
    }
    float4 _o = r[0];
    return (_o == _o) ? _o : (float4)0;
}

/* fp_addr=0x00004241 vmoff=0xC0004240 raw: B0 00 2F 06 5C 01 1C 9D 00 02 00 00 C8 00 3F E1 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
    float4 t2 : SV_TARGET2;
    float4 t3 : SV_TARGET3;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[3].SampleLevel(rsx_samp[3], ((input.tc1).zwzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).zwzz).xy)); r[3].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((float4(-1,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[3]).xxxx) >  (-((r[3]).yyyy)))); h[0].z = _v.z; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz); r[2].x = _v.x; }
    { float4 _v = (float4)((r[0]).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) <  ((float4(14,0,0,0)).xxxx))); h[1].w = _v.w; }
    { float4 _v = (float4)((float4)(((h[0]).zzzz) == ((float4(0,0,0,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz);
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[1]).xyzw));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)((-((r[3]).wwww)) + ((float4(1,0,0,0)).xxxx)); r[2].y = _v.y; }
    { float4 _v = (float4)((float4(65504,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      r[0].x = (_p.x != 0.0) ? _v.x : r[0].x;
    }
    { float4 _v = (float4)((input.tc0).xxxy); r[0].zw = _v.zw; }
    { float4 _v = (float4)((h[0]).zzzz);
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[0]).xxxx)); r[3].z = _v.z; }
    { float4 _v = (float4)(((r[3]).zzzz) * ((float4(0,1,0,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((r[0]).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[1]).wwww) * ((float4(1,0,0,0)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xxxx) * ((float4(-5.82079e-11,0,0.999,1)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + ((float4(9.31323e-10,3.72529e-09,-9.99,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) / ((r[1]).zzzz).x); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].w = (_p.w != 0.0) ? _v.w : r[4].w;
    }
    { float4 _v = (float4)(((r[0]).zwzz) + (-((r[0]).xyzw))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[3]).xxxy) * ((float4(2,-1,0,0)).xxxx) + ((float4(2,-1,0,0)).yyyy)); h[1].zw = _v.zw; }
    { float4 _v = (float4)(((r[0]).xxxy) * ((float4(38.6523,-21.7419,0,0)).xxxy));
      float4 _p = (float4)((cc0).wwww == (float4)0.0);
      h[1].zw = (_p.zw != 0.0) ? _v.zw : h[1].zw;
    }
    { float4 _v = (float4)((float4(0,0,0,0)).zzzz); h[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)) * 2.0; r[4].xy = _v.xy; }
    { float4 _v = (float4)(dot(((h[1]).zwzz).xy, ((h[1]).zwzz).xy)); h[1].x = _v.x; }
    { float4 _v = (float4)((float4)(((h[1]).xxxx) >  ((float4(1,0,0,0)).xxxx)));
      cc0.y = _v.y;
    }
    { float4 _v = (float4)((input.tc1).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)((h[1]).xyzw); h[0].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) + (-((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)));
      float4 _p = (float4)((cc0).xxxx > (float4)0.0);
      h[0].xy = (_p.xy != 0.0) ? _v.xy : h[0].xy;
    }
    { float4 _v = (float4)((abs((h[1]).xyzw) > 0.0 ? ((h[1]).xyzw) / sqrt(abs(((h[1]).xyzw).x)) : (float4)0.0));
      float4 _p = (float4)((cc0).yyyy != (float4)0.0);
      h[0].zw = (_p.zw != 0.0) ? _v.zw : h[0].zw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((h[0]).zwzz) * ((float4(0.0125,0.0222222,0.1,0.05625)).xyxx) + ((h[0]).xyzw)); r[4].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[4]).wwww) + ((r[1]).xyzw)); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx); r[1].x = _v.x; }
    { float4 _v = (float4)((float4(-0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(min(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[1]).xxxx) + ((r[1]).zwzz)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.6,0,0,1)).xxxx); r[2].w = _v.w; }
    { float4 _v = (float4)(min(((r[1]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[2].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].w = (_p.w != 0.0) ? _v.w : r[2].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[5].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[2]).xxxy), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((r[1]).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[2]).wwww) + ((r[1]).xyzw)); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[3].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((h[3]).xyzw).xy, ((h[3]).xyzw).xy)); r[2].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].w = (_p.w != 0.0) ? _v.w : r[1].w;
    }
    { float4 _v = (float4)((-((r[2]).xyzw)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].x = _v.x; }
    { float4 _v = (float4)(dot(((h[5]).xyzw).xy, ((h[5]).xyzw).xy)); r[1].x = _v.x; }
    { float4 _v = (float4)((-((r[1]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].w = _v.w; }
    { float4 _v = (float4)((r[2]).xyzw); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[0]).wwww)); r[5].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[1]).xyzw)); r[2].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).zwzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).wwww) + ((r[0]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)((float4)((abs((r[1]).xyzw)) <  ((float4(5.55112e-17,0.0005,4,0)).xxxx)));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(min(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[5].y = _v.y; }
    { float4 _v = (float4)(((r[0]).wwww) + ((r[2]).wwww)); h[11].x = _v.x; }
    { float4 _v = (float4)(max(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[5].y = (_p.y != 0.0) ? _v.y : r[5].y;
    }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).xxxx) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[5]).xxxx) + ((h[11]).xxxx)); h[9].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[3]).zwzz).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[0]).xxxy)); h[11].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[3]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((h[11]).zwzz).xy, ((h[11]).zwzz).xy)); r[5].x = _v.x; }
    { float4 _v = (float4)((-((r[5]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).yyyy)); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((input.tc0).zwzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[7].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).yyyy); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[2]).wwww) + ((h[9]).wwww)); h[5].z = _v.z; }
    { float4 _v = (float4)((abs((r[1]).xyzw)) + (-((float4(5.55112e-17,0.0005,4,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((abs((h[0]).wwww)) * ((float4(5.55112e-17,0.0005,4,0)).yyyy)); _v = saturate(_v); h[9].x = _v.x; }
    { float4 _v = (float4)(log2(((h[9]).xyzw).x)); h[9].x = _v.x; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      h[0].x = (_p.x != 0.0) ? _v.x : h[0].x;
    }
    { float4 _v = (float4)(((h[9]).xxxx) * ((float4(5.55112e-17,0.0005,4,0)).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].y = _v.y; }
    { float4 _v = (float4)(min(((h[0]).xyzw), ((h[0]).yyyy))); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((float4(80,45,0,0)).xxxy)); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((h[0]).xyzw), ((float4(5.55112e-17,0.0005,4,0)).wwww))); h[1].x = _v.x; }
    { float4 _v = (float4)((-((h[1]).xxxx)) + ((float4(0,1,0,0)).yyyy)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.8,0,0,1)).xxxx); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((h[7]).xyzw)); h[3].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((h[7]).xyzw)); h[3].w = _v.w; }
    { float4 _v = (float4)((input.tc1).zwzz); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(-0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].z = (_p.z != 0.0) ? _v.z : r[0].z;
    }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[0]).zzzz) + ((r[0]).xyzw)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyxx))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[0]).xyzw).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[1]).xxxy)); h[2].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[0]).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].x = (_p.x != 0.0) ? _v.x : r[4].x;
    }
    { float4 _v = (float4)(dot(((h[2]).zwzz).xy, ((h[2]).zwzz).xy)); r[4].y = _v.y; }
    { float4 _v = (float4)(((h[3]).xyzw) / ((h[3]).wwww).x); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)((-((r[4]).yyyy)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((r[4]).zwzz).xy, ((r[4]).zwzz).xy)); r[1].z = _v.z; }
    { float4 _v = (float4)(((r[1]).wwww) * ((r[4]).xyzw)); r[3].x = _v.x; }
    { float4 _v = (float4)((abs(abs((r[1]).zzzz)) > 0.0 ? (abs((r[1]).zzzz)) / sqrt(abs(((r[1]).zzzz).x)) : (float4)0.0)); _v = saturate(_v); h[5].w = _v.w; }
    { float4 _v = (float4)(((h[5]).xyzw) * ((r[0]).xyzw)); h[2].w = _v.w; }
    { float4 _v = (float4)((-((h[2]).xyzw)) * ((r[0]).xyzw) + ((r[0]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[3]).xxxx) + ((r[2]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[3]).xxxx) + ((h[5]).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) / ((h[0]).wwww).x); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((h[2]).xyzw))); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[2]).wwww) * ((h[0]).xyzw) + ((h[2]).xyzw)) / 4.0; r[0].xyz = _v.xyz; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    float4 _o2 = r[3];
    _out.t2 = (_o2 == _o2) ? _o2 : (float4)0;
    float4 _o3 = r[4];
    _out.t3 = (_o3 == _o3) ? _o3 : (float4)0;
    return _out;
}

/* fp_addr=0x00001441 vmoff=0xC0001440 raw: B0 00 2F 06 5C 01 1C 9D 00 02 00 00 C8 00 3F E1 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
    float4 t2 : SV_TARGET2;
    float4 t3 : SV_TARGET3;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[3].SampleLevel(rsx_samp[3], ((input.tc1).zwzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).zwzz).xy)); r[3].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((float4(-1,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[3]).xxxx) >  (-((r[3]).yyyy)))); h[0].z = _v.z; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz); r[2].x = _v.x; }
    { float4 _v = (float4)((r[0]).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) <  ((float4(14,0,0,0)).xxxx))); h[1].w = _v.w; }
    { float4 _v = (float4)((float4)(((h[0]).zzzz) == ((float4(0,0,0,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz);
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[1]).xyzw));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)((-((r[3]).wwww)) + ((float4(1,0,0,0)).xxxx)); r[2].y = _v.y; }
    { float4 _v = (float4)((float4(65504,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      r[0].x = (_p.x != 0.0) ? _v.x : r[0].x;
    }
    { float4 _v = (float4)((input.tc0).xxxy); r[0].zw = _v.zw; }
    { float4 _v = (float4)((h[0]).zzzz);
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[0]).xxxx)); r[3].z = _v.z; }
    { float4 _v = (float4)(((r[3]).zzzz) * ((float4(0,1,0,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((r[0]).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[1]).wwww) * ((float4(1,0,0,0)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xxxx) * ((float4(0,8.4771e-07,0.999,1)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + ((float4(0,-7.62939e-06,-9.99,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) / ((r[1]).zzzz).x); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].w = (_p.w != 0.0) ? _v.w : r[4].w;
    }
    { float4 _v = (float4)(((r[0]).zwzz) + (-((r[0]).xyzw))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[3]).xxxy) * ((float4(2,-1,0,0)).xxxx) + ((float4(2,-1,0,0)).yyyy)); h[1].zw = _v.zw; }
    { float4 _v = (float4)(((r[0]).xxxy) * ((float4(0,0,0,0)).xxxy));
      float4 _p = (float4)((cc0).wwww == (float4)0.0);
      h[1].zw = (_p.zw != 0.0) ? _v.zw : h[1].zw;
    }
    { float4 _v = (float4)((float4(0,0,0,0)).zzzz); h[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)) * 2.0; r[4].xy = _v.xy; }
    { float4 _v = (float4)(dot(((h[1]).zwzz).xy, ((h[1]).zwzz).xy)); h[1].x = _v.x; }
    { float4 _v = (float4)((float4)(((h[1]).xxxx) >  ((float4(1,0,0,0)).xxxx)));
      cc0.y = _v.y;
    }
    { float4 _v = (float4)((input.tc1).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)((h[1]).xyzw); h[0].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) + (-((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)));
      float4 _p = (float4)((cc0).xxxx > (float4)0.0);
      h[0].xy = (_p.xy != 0.0) ? _v.xy : h[0].xy;
    }
    { float4 _v = (float4)((abs((h[1]).xyzw) > 0.0 ? ((h[1]).xyzw) / sqrt(abs(((h[1]).xyzw).x)) : (float4)0.0));
      float4 _p = (float4)((cc0).yyyy != (float4)0.0);
      h[0].zw = (_p.zw != 0.0) ? _v.zw : h[0].zw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((h[0]).zwzz) * ((float4(0.0125,0.0222222,0.1,0.05625)).xyxx) + ((h[0]).xyzw)); r[4].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[4]).wwww) + ((r[1]).xyzw)); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx); r[1].x = _v.x; }
    { float4 _v = (float4)((float4(-0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(min(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[1]).xxxx) + ((r[1]).zwzz)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.6,0,0,1)).xxxx); r[2].w = _v.w; }
    { float4 _v = (float4)(min(((r[1]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[2].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].w = (_p.w != 0.0) ? _v.w : r[2].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[5].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[2]).xxxy), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((r[1]).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[2]).wwww) + ((r[1]).xyzw)); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[3].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((h[3]).xyzw).xy, ((h[3]).xyzw).xy)); r[2].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].w = (_p.w != 0.0) ? _v.w : r[1].w;
    }
    { float4 _v = (float4)((-((r[2]).xyzw)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].x = _v.x; }
    { float4 _v = (float4)(dot(((h[5]).xyzw).xy, ((h[5]).xyzw).xy)); r[1].x = _v.x; }
    { float4 _v = (float4)((-((r[1]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].w = _v.w; }
    { float4 _v = (float4)((r[2]).xyzw); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[0]).wwww)); r[5].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[1]).xyzw)); r[2].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).zwzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).wwww) + ((r[0]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)((float4)((abs((r[1]).xyzw)) <  ((float4(0,0.0005,4,0)).xxxx)));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(min(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[5].y = _v.y; }
    { float4 _v = (float4)(((r[0]).wwww) + ((r[2]).wwww)); h[11].x = _v.x; }
    { float4 _v = (float4)(max(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[5].y = (_p.y != 0.0) ? _v.y : r[5].y;
    }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).xxxx) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[5]).xxxx) + ((h[11]).xxxx)); h[9].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[3]).zwzz).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[0]).xxxy)); h[11].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[3]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((h[11]).zwzz).xy, ((h[11]).zwzz).xy)); r[5].x = _v.x; }
    { float4 _v = (float4)((-((r[5]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).yyyy)); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((input.tc0).zwzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[7].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).yyyy); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[2]).wwww) + ((h[9]).wwww)); h[5].z = _v.z; }
    { float4 _v = (float4)((abs((r[1]).xyzw)) + (-((float4(0,0.0005,4,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((abs((h[0]).wwww)) * ((float4(0,0.0005,4,0)).yyyy)); _v = saturate(_v); h[9].x = _v.x; }
    { float4 _v = (float4)(log2(((h[9]).xyzw).x)); h[9].x = _v.x; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      h[0].x = (_p.x != 0.0) ? _v.x : h[0].x;
    }
    { float4 _v = (float4)(((h[9]).xxxx) * ((float4(0,0.0005,4,0)).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].y = _v.y; }
    { float4 _v = (float4)(min(((h[0]).xyzw), ((h[0]).yyyy))); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((float4(80,45,0,0)).xxxy)); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((h[0]).xyzw), ((float4(0,0.0005,4,0)).wwww))); h[1].x = _v.x; }
    { float4 _v = (float4)((-((h[1]).xxxx)) + ((float4(0,1,0,0)).yyyy)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.8,0,0,1)).xxxx); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((h[7]).xyzw)); h[3].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((h[7]).xyzw)); h[3].w = _v.w; }
    { float4 _v = (float4)((input.tc1).zwzz); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(-0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].z = (_p.z != 0.0) ? _v.z : r[0].z;
    }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[0]).zzzz) + ((r[0]).xyzw)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyxx))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[0]).xyzw).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[1]).xxxy)); h[2].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[0]).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].x = (_p.x != 0.0) ? _v.x : r[4].x;
    }
    { float4 _v = (float4)(dot(((h[2]).zwzz).xy, ((h[2]).zwzz).xy)); r[4].y = _v.y; }
    { float4 _v = (float4)(((h[3]).xyzw) / ((h[3]).wwww).x); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)((-((r[4]).yyyy)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((r[4]).zwzz).xy, ((r[4]).zwzz).xy)); r[1].z = _v.z; }
    { float4 _v = (float4)(((r[1]).wwww) * ((r[4]).xyzw)); r[3].x = _v.x; }
    { float4 _v = (float4)((abs(abs((r[1]).zzzz)) > 0.0 ? (abs((r[1]).zzzz)) / sqrt(abs(((r[1]).zzzz).x)) : (float4)0.0)); _v = saturate(_v); h[5].w = _v.w; }
    { float4 _v = (float4)(((h[5]).xyzw) * ((r[0]).xyzw)); h[2].w = _v.w; }
    { float4 _v = (float4)((-((h[2]).xyzw)) * ((r[0]).xyzw) + ((r[0]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[3]).xxxx) + ((r[2]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[3]).xxxx) + ((h[5]).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) / ((h[0]).wwww).x); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((h[2]).xyzw))); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[2]).wwww) * ((h[0]).xyzw) + ((h[2]).xyzw)) / 4.0; r[0].xyz = _v.xyz; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    float4 _o2 = r[3];
    _out.t2 = (_o2 == _o2) ? _o2 : (float4)0;
    float4 _o3 = r[4];
    _out.t3 = (_o3 == _o3) ? _o3 : (float4)0;
    return _out;
}

/* fp_addr=0x00004241 vmoff=0xC0004240 raw: B0 00 2F 06 5C 01 1C 9D 00 02 00 00 C8 00 3F E1 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
    float4 t2 : SV_TARGET2;
    float4 t3 : SV_TARGET3;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[3].SampleLevel(rsx_samp[3], ((input.tc1).zwzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).zwzz).xy)); r[3].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((float4(-1,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[3]).xxxx) >  (-((r[3]).yyyy)))); h[0].z = _v.z; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz); r[2].x = _v.x; }
    { float4 _v = (float4)((r[0]).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) <  ((float4(14,0,0,0)).xxxx))); h[1].w = _v.w; }
    { float4 _v = (float4)((float4)(((h[0]).zzzz) == ((float4(0,0,0,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz);
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[1]).xyzw));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)((-((r[3]).wwww)) + ((float4(1,0,0,0)).xxxx)); r[2].y = _v.y; }
    { float4 _v = (float4)((float4(65504,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      r[0].x = (_p.x != 0.0) ? _v.x : r[0].x;
    }
    { float4 _v = (float4)((input.tc0).xxxy); r[0].zw = _v.zw; }
    { float4 _v = (float4)((h[0]).zzzz);
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[0]).xxxx)); r[3].z = _v.z; }
    { float4 _v = (float4)(((r[3]).zzzz) * ((float4(0,1,0,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((r[0]).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[1]).wwww) * ((float4(1,0,0,0)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xxxx) * ((float4(-5.82079e-11,0,0.999,1)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + ((float4(9.31323e-10,3.72529e-09,-9.99,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) / ((r[1]).zzzz).x); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].w = (_p.w != 0.0) ? _v.w : r[4].w;
    }
    { float4 _v = (float4)(((r[0]).zwzz) + (-((r[0]).xyzw))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[3]).xxxy) * ((float4(2,-1,0,0)).xxxx) + ((float4(2,-1,0,0)).yyyy)); h[1].zw = _v.zw; }
    { float4 _v = (float4)(((r[0]).xxxy) * ((float4(38.6523,-21.7419,0,0)).xxxy));
      float4 _p = (float4)((cc0).wwww == (float4)0.0);
      h[1].zw = (_p.zw != 0.0) ? _v.zw : h[1].zw;
    }
    { float4 _v = (float4)((float4(0,0,0,0)).zzzz); h[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)) * 2.0; r[4].xy = _v.xy; }
    { float4 _v = (float4)(dot(((h[1]).zwzz).xy, ((h[1]).zwzz).xy)); h[1].x = _v.x; }
    { float4 _v = (float4)((float4)(((h[1]).xxxx) >  ((float4(1,0,0,0)).xxxx)));
      cc0.y = _v.y;
    }
    { float4 _v = (float4)((input.tc1).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)((h[1]).xyzw); h[0].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) + (-((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)));
      float4 _p = (float4)((cc0).xxxx > (float4)0.0);
      h[0].xy = (_p.xy != 0.0) ? _v.xy : h[0].xy;
    }
    { float4 _v = (float4)((abs((h[1]).xyzw) > 0.0 ? ((h[1]).xyzw) / sqrt(abs(((h[1]).xyzw).x)) : (float4)0.0));
      float4 _p = (float4)((cc0).yyyy != (float4)0.0);
      h[0].zw = (_p.zw != 0.0) ? _v.zw : h[0].zw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((h[0]).zwzz) * ((float4(0.0125,0.0222222,0.1,0.05625)).xyxx) + ((h[0]).xyzw)); r[4].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[4]).wwww) + ((r[1]).xyzw)); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx); r[1].x = _v.x; }
    { float4 _v = (float4)((float4(-0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(min(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[1]).xxxx) + ((r[1]).zwzz)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.6,0,0,1)).xxxx); r[2].w = _v.w; }
    { float4 _v = (float4)(min(((r[1]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[2].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].w = (_p.w != 0.0) ? _v.w : r[2].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[5].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[2]).xxxy), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((r[1]).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[2]).wwww) + ((r[1]).xyzw)); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[3].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((h[3]).xyzw).xy, ((h[3]).xyzw).xy)); r[2].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].w = (_p.w != 0.0) ? _v.w : r[1].w;
    }
    { float4 _v = (float4)((-((r[2]).xyzw)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].x = _v.x; }
    { float4 _v = (float4)(dot(((h[5]).xyzw).xy, ((h[5]).xyzw).xy)); r[1].x = _v.x; }
    { float4 _v = (float4)((-((r[1]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].w = _v.w; }
    { float4 _v = (float4)((r[2]).xyzw); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[0]).wwww)); r[5].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[1]).xyzw)); r[2].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).zwzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).wwww) + ((r[0]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)((float4)((abs((r[1]).xyzw)) <  ((float4(5.55112e-17,0.0005,4,0)).xxxx)));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(min(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[5].y = _v.y; }
    { float4 _v = (float4)(((r[0]).wwww) + ((r[2]).wwww)); h[11].x = _v.x; }
    { float4 _v = (float4)(max(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[5].y = (_p.y != 0.0) ? _v.y : r[5].y;
    }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).xxxx) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[5]).xxxx) + ((h[11]).xxxx)); h[9].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[3]).zwzz).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[0]).xxxy)); h[11].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[3]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((h[11]).zwzz).xy, ((h[11]).zwzz).xy)); r[5].x = _v.x; }
    { float4 _v = (float4)((-((r[5]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).yyyy)); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((input.tc0).zwzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[7].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).yyyy); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[2]).wwww) + ((h[9]).wwww)); h[5].z = _v.z; }
    { float4 _v = (float4)((abs((r[1]).xyzw)) + (-((float4(5.55112e-17,0.0005,4,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((abs((h[0]).wwww)) * ((float4(5.55112e-17,0.0005,4,0)).yyyy)); _v = saturate(_v); h[9].x = _v.x; }
    { float4 _v = (float4)(log2(((h[9]).xyzw).x)); h[9].x = _v.x; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      h[0].x = (_p.x != 0.0) ? _v.x : h[0].x;
    }
    { float4 _v = (float4)(((h[9]).xxxx) * ((float4(5.55112e-17,0.0005,4,0)).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].y = _v.y; }
    { float4 _v = (float4)(min(((h[0]).xyzw), ((h[0]).yyyy))); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((float4(80,45,0,0)).xxxy)); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((h[0]).xyzw), ((float4(5.55112e-17,0.0005,4,0)).wwww))); h[1].x = _v.x; }
    { float4 _v = (float4)((-((h[1]).xxxx)) + ((float4(0,1,0,0)).yyyy)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.8,0,0,1)).xxxx); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((h[7]).xyzw)); h[3].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((h[7]).xyzw)); h[3].w = _v.w; }
    { float4 _v = (float4)((input.tc1).zwzz); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(-0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].z = (_p.z != 0.0) ? _v.z : r[0].z;
    }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[0]).zzzz) + ((r[0]).xyzw)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyxx))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[0]).xyzw).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[1]).xxxy)); h[2].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[0]).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].x = (_p.x != 0.0) ? _v.x : r[4].x;
    }
    { float4 _v = (float4)(dot(((h[2]).zwzz).xy, ((h[2]).zwzz).xy)); r[4].y = _v.y; }
    { float4 _v = (float4)(((h[3]).xyzw) / ((h[3]).wwww).x); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)((-((r[4]).yyyy)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((r[4]).zwzz).xy, ((r[4]).zwzz).xy)); r[1].z = _v.z; }
    { float4 _v = (float4)(((r[1]).wwww) * ((r[4]).xyzw)); r[3].x = _v.x; }
    { float4 _v = (float4)((abs(abs((r[1]).zzzz)) > 0.0 ? (abs((r[1]).zzzz)) / sqrt(abs(((r[1]).zzzz).x)) : (float4)0.0)); _v = saturate(_v); h[5].w = _v.w; }
    { float4 _v = (float4)(((h[5]).xyzw) * ((r[0]).xyzw)); h[2].w = _v.w; }
    { float4 _v = (float4)((-((h[2]).xyzw)) * ((r[0]).xyzw) + ((r[0]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[3]).xxxx) + ((r[2]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[3]).xxxx) + ((h[5]).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) / ((h[0]).wwww).x); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((h[2]).xyzw))); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[2]).wwww) * ((h[0]).xyzw) + ((h[2]).xyzw)) / 4.0; r[0].xyz = _v.xyz; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    float4 _o2 = r[3];
    _out.t2 = (_o2 == _o2) ? _o2 : (float4)0;
    float4 _o3 = r[4];
    _out.t3 = (_o3 == _o3) ? _o3 : (float4)0;
    return _out;
}

/* fp_addr=0x00007041 vmoff=0xC0007040 raw: B0 00 2F 06 5C 01 1C 9D 00 02 00 00 C8 00 3F E1 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
    float4 t2 : SV_TARGET2;
    float4 t3 : SV_TARGET3;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[3].SampleLevel(rsx_samp[3], ((input.tc1).zwzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).zwzz).xy)); r[3].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((float4(-1,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[3]).xxxx) >  (-((r[3]).yyyy)))); h[0].z = _v.z; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz); r[2].x = _v.x; }
    { float4 _v = (float4)((r[0]).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) <  ((float4(14,0,0,0)).xxxx))); h[1].w = _v.w; }
    { float4 _v = (float4)((float4)(((h[0]).zzzz) == ((float4(0,0,0,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz);
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[1]).xyzw));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)((-((r[3]).wwww)) + ((float4(1,0,0,0)).xxxx)); r[2].y = _v.y; }
    { float4 _v = (float4)((float4(65504,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      r[0].x = (_p.x != 0.0) ? _v.x : r[0].x;
    }
    { float4 _v = (float4)((input.tc0).xxxy); r[0].zw = _v.zw; }
    { float4 _v = (float4)((h[0]).zzzz);
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[0]).xxxx)); r[3].z = _v.z; }
    { float4 _v = (float4)(((r[3]).zzzz) * ((float4(0,1,0,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((r[0]).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[1]).wwww) * ((float4(1,0,0,0)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xxxx) * ((float4(0,0,0.999,1)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + ((float4(-15.9905,-83.2396,-9.99,9.53107e-07)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) / ((r[1]).zzzz).x); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].w = (_p.w != 0.0) ? _v.w : r[4].w;
    }
    { float4 _v = (float4)(((r[0]).zwzz) + (-((r[0]).xyzw))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[3]).xxxy) * ((float4(2,-1,0,0)).xxxx) + ((float4(2,-1,0,0)).yyyy)); h[1].zw = _v.zw; }
    { float4 _v = (float4)(((r[0]).xxxy) * ((float4(38.6352,-21.7323,0,0)).xxxy));
      float4 _p = (float4)((cc0).wwww == (float4)0.0);
      h[1].zw = (_p.zw != 0.0) ? _v.zw : h[1].zw;
    }
    { float4 _v = (float4)((float4(0,0,0,0)).zzzz); h[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)) * 2.0; r[4].xy = _v.xy; }
    { float4 _v = (float4)(dot(((h[1]).zwzz).xy, ((h[1]).zwzz).xy)); h[1].x = _v.x; }
    { float4 _v = (float4)((float4)(((h[1]).xxxx) >  ((float4(1,0,0,0)).xxxx)));
      cc0.y = _v.y;
    }
    { float4 _v = (float4)((input.tc1).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)((h[1]).xyzw); h[0].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) + (-((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)));
      float4 _p = (float4)((cc0).xxxx > (float4)0.0);
      h[0].xy = (_p.xy != 0.0) ? _v.xy : h[0].xy;
    }
    { float4 _v = (float4)((abs((h[1]).xyzw) > 0.0 ? ((h[1]).xyzw) / sqrt(abs(((h[1]).xyzw).x)) : (float4)0.0));
      float4 _p = (float4)((cc0).yyyy != (float4)0.0);
      h[0].zw = (_p.zw != 0.0) ? _v.zw : h[0].zw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((h[0]).zwzz) * ((float4(0.0125,0.0222222,0.1,0.05625)).xyxx) + ((h[0]).xyzw)); r[4].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[4]).wwww) + ((r[1]).xyzw)); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx); r[1].x = _v.x; }
    { float4 _v = (float4)((float4(-0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(min(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[1]).xxxx) + ((r[1]).zwzz)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.6,0,0,1)).xxxx); r[2].w = _v.w; }
    { float4 _v = (float4)(min(((r[1]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[2].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].w = (_p.w != 0.0) ? _v.w : r[2].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[5].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[2]).xxxy), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((r[1]).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[2]).wwww) + ((r[1]).xyzw)); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[3].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((h[3]).xyzw).xy, ((h[3]).xyzw).xy)); r[2].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].w = (_p.w != 0.0) ? _v.w : r[1].w;
    }
    { float4 _v = (float4)((-((r[2]).xyzw)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].x = _v.x; }
    { float4 _v = (float4)(dot(((h[5]).xyzw).xy, ((h[5]).xyzw).xy)); r[1].x = _v.x; }
    { float4 _v = (float4)((-((r[1]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].w = _v.w; }
    { float4 _v = (float4)((r[2]).xyzw); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[0]).wwww)); r[5].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[1]).xyzw)); r[2].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).zwzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).wwww) + ((r[0]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)((float4)((abs((r[1]).xyzw)) <  ((float4(0,0.0005,4,0)).xxxx)));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(min(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[5].y = _v.y; }
    { float4 _v = (float4)(((r[0]).wwww) + ((r[2]).wwww)); h[11].x = _v.x; }
    { float4 _v = (float4)(max(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[5].y = (_p.y != 0.0) ? _v.y : r[5].y;
    }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).xxxx) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[5]).xxxx) + ((h[11]).xxxx)); h[9].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[3]).zwzz).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[0]).xxxy)); h[11].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[3]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((h[11]).zwzz).xy, ((h[11]).zwzz).xy)); r[5].x = _v.x; }
    { float4 _v = (float4)((-((r[5]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).yyyy)); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((input.tc0).zwzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[7].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).yyyy); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[2]).wwww) + ((h[9]).wwww)); h[5].z = _v.z; }
    { float4 _v = (float4)((abs((r[1]).xyzw)) + (-((float4(0,0.0005,4,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((abs((h[0]).wwww)) * ((float4(0,0.0005,4,0)).yyyy)); _v = saturate(_v); h[9].x = _v.x; }
    { float4 _v = (float4)(log2(((h[9]).xyzw).x)); h[9].x = _v.x; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      h[0].x = (_p.x != 0.0) ? _v.x : h[0].x;
    }
    { float4 _v = (float4)(((h[9]).xxxx) * ((float4(0,0.0005,4,0)).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].y = _v.y; }
    { float4 _v = (float4)(min(((h[0]).xyzw), ((h[0]).yyyy))); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((float4(80,45,0,0)).xxxy)); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((h[0]).xyzw), ((float4(0,0.0005,4,0)).wwww))); h[1].x = _v.x; }
    { float4 _v = (float4)((-((h[1]).xxxx)) + ((float4(0,1,0,0)).yyyy)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.8,0,0,1)).xxxx); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((h[7]).xyzw)); h[3].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((h[7]).xyzw)); h[3].w = _v.w; }
    { float4 _v = (float4)((input.tc1).zwzz); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(-0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].z = (_p.z != 0.0) ? _v.z : r[0].z;
    }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[0]).zzzz) + ((r[0]).xyzw)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyxx))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[0]).xyzw).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[1]).xxxy)); h[2].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[0]).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].x = (_p.x != 0.0) ? _v.x : r[4].x;
    }
    { float4 _v = (float4)(dot(((h[2]).zwzz).xy, ((h[2]).zwzz).xy)); r[4].y = _v.y; }
    { float4 _v = (float4)(((h[3]).xyzw) / ((h[3]).wwww).x); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)((-((r[4]).yyyy)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((r[4]).zwzz).xy, ((r[4]).zwzz).xy)); r[1].z = _v.z; }
    { float4 _v = (float4)(((r[1]).wwww) * ((r[4]).xyzw)); r[3].x = _v.x; }
    { float4 _v = (float4)((abs(abs((r[1]).zzzz)) > 0.0 ? (abs((r[1]).zzzz)) / sqrt(abs(((r[1]).zzzz).x)) : (float4)0.0)); _v = saturate(_v); h[5].w = _v.w; }
    { float4 _v = (float4)(((h[5]).xyzw) * ((r[0]).xyzw)); h[2].w = _v.w; }
    { float4 _v = (float4)((-((h[2]).xyzw)) * ((r[0]).xyzw) + ((r[0]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[3]).xxxx) + ((r[2]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[3]).xxxx) + ((h[5]).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) / ((h[0]).wwww).x); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((h[2]).xyzw))); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[2]).wwww) * ((h[0]).xyzw) + ((h[2]).xyzw)) / 4.0; r[0].xyz = _v.xyz; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    float4 _o2 = r[3];
    _out.t2 = (_o2 == _o2) ? _o2 : (float4)0;
    float4 _o3 = r[4];
    _out.t3 = (_o3 == _o3) ? _o3 : (float4)0;
    return _out;
}

/* fp_addr=0x00007041 vmoff=0xC0007040 raw: B0 00 2F 06 5C 01 1C 9D 00 02 00 00 C8 00 3F E1 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
    float4 t2 : SV_TARGET2;
    float4 t3 : SV_TARGET3;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[3].SampleLevel(rsx_samp[3], ((input.tc1).zwzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).zwzz).xy)); r[3].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((float4(-1,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[3]).xxxx) >  (-((r[3]).yyyy)))); h[0].z = _v.z; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz); r[2].x = _v.x; }
    { float4 _v = (float4)((r[0]).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) <  ((float4(14,0,0,0)).xxxx))); h[1].w = _v.w; }
    { float4 _v = (float4)((float4)(((h[0]).zzzz) == ((float4(0,0,0,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz);
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[1]).xyzw));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)((-((r[3]).wwww)) + ((float4(1,0,0,0)).xxxx)); r[2].y = _v.y; }
    { float4 _v = (float4)((float4(65504,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      r[0].x = (_p.x != 0.0) ? _v.x : r[0].x;
    }
    { float4 _v = (float4)((input.tc0).xxxy); r[0].zw = _v.zw; }
    { float4 _v = (float4)((h[0]).zzzz);
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[0]).xxxx)); r[3].z = _v.z; }
    { float4 _v = (float4)(((r[3]).zzzz) * ((float4(0,1,0,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((r[0]).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[1]).wwww) * ((float4(1,0,0,0)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xxxx) * ((float4(0,0,0.999,1)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + ((float4(-15.9905,-83.2396,-9.99,9.53107e-07)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) / ((r[1]).zzzz).x); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].w = (_p.w != 0.0) ? _v.w : r[4].w;
    }
    { float4 _v = (float4)(((r[0]).zwzz) + (-((r[0]).xyzw))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[3]).xxxy) * ((float4(2,-1,0,0)).xxxx) + ((float4(2,-1,0,0)).yyyy)); h[1].zw = _v.zw; }
    { float4 _v = (float4)(((r[0]).xxxy) * ((float4(38.6352,-21.7323,0,0)).xxxy));
      float4 _p = (float4)((cc0).wwww == (float4)0.0);
      h[1].zw = (_p.zw != 0.0) ? _v.zw : h[1].zw;
    }
    { float4 _v = (float4)((float4(0,0,0,0)).zzzz); h[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)) * 2.0; r[4].xy = _v.xy; }
    { float4 _v = (float4)(dot(((h[1]).zwzz).xy, ((h[1]).zwzz).xy)); h[1].x = _v.x; }
    { float4 _v = (float4)((float4)(((h[1]).xxxx) >  ((float4(1,0,0,0)).xxxx)));
      cc0.y = _v.y;
    }
    { float4 _v = (float4)((input.tc1).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)((h[1]).xyzw); h[0].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) + (-((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)));
      float4 _p = (float4)((cc0).xxxx > (float4)0.0);
      h[0].xy = (_p.xy != 0.0) ? _v.xy : h[0].xy;
    }
    { float4 _v = (float4)((abs((h[1]).xyzw) > 0.0 ? ((h[1]).xyzw) / sqrt(abs(((h[1]).xyzw).x)) : (float4)0.0));
      float4 _p = (float4)((cc0).yyyy != (float4)0.0);
      h[0].zw = (_p.zw != 0.0) ? _v.zw : h[0].zw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((h[0]).zwzz) * ((float4(0.0125,0.0222222,0.1,0.05625)).xyxx) + ((h[0]).xyzw)); r[4].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[4]).wwww) + ((r[1]).xyzw)); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx); r[1].x = _v.x; }
    { float4 _v = (float4)((float4(-0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(min(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[1]).xxxx) + ((r[1]).zwzz)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.6,0,0,1)).xxxx); r[2].w = _v.w; }
    { float4 _v = (float4)(min(((r[1]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[2].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].w = (_p.w != 0.0) ? _v.w : r[2].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[5].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[2]).xxxy), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((r[1]).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[2]).wwww) + ((r[1]).xyzw)); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[3].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((h[3]).xyzw).xy, ((h[3]).xyzw).xy)); r[2].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].w = (_p.w != 0.0) ? _v.w : r[1].w;
    }
    { float4 _v = (float4)((-((r[2]).xyzw)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].x = _v.x; }
    { float4 _v = (float4)(dot(((h[5]).xyzw).xy, ((h[5]).xyzw).xy)); r[1].x = _v.x; }
    { float4 _v = (float4)((-((r[1]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].w = _v.w; }
    { float4 _v = (float4)((r[2]).xyzw); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[0]).wwww)); r[5].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[1]).xyzw)); r[2].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).zwzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).wwww) + ((r[0]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)((float4)((abs((r[1]).xyzw)) <  ((float4(0,0.0005,4,0)).xxxx)));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(min(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[5].y = _v.y; }
    { float4 _v = (float4)(((r[0]).wwww) + ((r[2]).wwww)); h[11].x = _v.x; }
    { float4 _v = (float4)(max(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[5].y = (_p.y != 0.0) ? _v.y : r[5].y;
    }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).xxxx) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[5]).xxxx) + ((h[11]).xxxx)); h[9].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[3]).zwzz).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[0]).xxxy)); h[11].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[3]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((h[11]).zwzz).xy, ((h[11]).zwzz).xy)); r[5].x = _v.x; }
    { float4 _v = (float4)((-((r[5]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).yyyy)); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((input.tc0).zwzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[7].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).yyyy); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[2]).wwww) + ((h[9]).wwww)); h[5].z = _v.z; }
    { float4 _v = (float4)((abs((r[1]).xyzw)) + (-((float4(0,0.0005,4,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((abs((h[0]).wwww)) * ((float4(0,0.0005,4,0)).yyyy)); _v = saturate(_v); h[9].x = _v.x; }
    { float4 _v = (float4)(log2(((h[9]).xyzw).x)); h[9].x = _v.x; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      h[0].x = (_p.x != 0.0) ? _v.x : h[0].x;
    }
    { float4 _v = (float4)(((h[9]).xxxx) * ((float4(0,0.0005,4,0)).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].y = _v.y; }
    { float4 _v = (float4)(min(((h[0]).xyzw), ((h[0]).yyyy))); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((float4(80,45,0,0)).xxxy)); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((h[0]).xyzw), ((float4(0,0.0005,4,0)).wwww))); h[1].x = _v.x; }
    { float4 _v = (float4)((-((h[1]).xxxx)) + ((float4(0,1,0,0)).yyyy)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.8,0,0,1)).xxxx); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((h[7]).xyzw)); h[3].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((h[7]).xyzw)); h[3].w = _v.w; }
    { float4 _v = (float4)((input.tc1).zwzz); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(-0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].z = (_p.z != 0.0) ? _v.z : r[0].z;
    }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[0]).zzzz) + ((r[0]).xyzw)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyxx))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[0]).xyzw).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[1]).xxxy)); h[2].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[0]).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].x = (_p.x != 0.0) ? _v.x : r[4].x;
    }
    { float4 _v = (float4)(dot(((h[2]).zwzz).xy, ((h[2]).zwzz).xy)); r[4].y = _v.y; }
    { float4 _v = (float4)(((h[3]).xyzw) / ((h[3]).wwww).x); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)((-((r[4]).yyyy)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((r[4]).zwzz).xy, ((r[4]).zwzz).xy)); r[1].z = _v.z; }
    { float4 _v = (float4)(((r[1]).wwww) * ((r[4]).xyzw)); r[3].x = _v.x; }
    { float4 _v = (float4)((abs(abs((r[1]).zzzz)) > 0.0 ? (abs((r[1]).zzzz)) / sqrt(abs(((r[1]).zzzz).x)) : (float4)0.0)); _v = saturate(_v); h[5].w = _v.w; }
    { float4 _v = (float4)(((h[5]).xyzw) * ((r[0]).xyzw)); h[2].w = _v.w; }
    { float4 _v = (float4)((-((h[2]).xyzw)) * ((r[0]).xyzw) + ((r[0]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[3]).xxxx) + ((r[2]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[3]).xxxx) + ((h[5]).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) / ((h[0]).wwww).x); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((h[2]).xyzw))); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[2]).wwww) * ((h[0]).xyzw) + ((h[2]).xyzw)) / 4.0; r[0].xyz = _v.xyz; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    float4 _o2 = r[3];
    _out.t2 = (_o2 == _o2) ? _o2 : (float4)0;
    float4 _o3 = r[4];
    _out.t3 = (_o3 == _o3) ? _o3 : (float4)0;
    return _out;
}

/* fp_addr=0x00009E41 vmoff=0xC0009E40 raw: B0 00 2F 06 5C 01 1C 9D 00 02 00 00 C8 00 3F E1 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 */
struct PSInput {
    float4 position : SV_POSITION; float4 col0 : COLOR0; float4 col1 : COLOR1;
    float4 fog : FOG;
    float4 tc0:TEXCOORD0; float4 tc1:TEXCOORD1; float4 tc2:TEXCOORD2; float4 tc3:TEXCOORD3;
    float4 tc4:TEXCOORD4; float4 tc5:TEXCOORD5; float4 tc6:TEXCOORD6; float4 tc7:TEXCOORD7;
};
Texture2D    rsx_tex[16] : register(t0);
SamplerState rsx_samp[16] : register(s0);
struct PSOutput {
    float4 t0 : SV_TARGET0;
    float4 t1 : SV_TARGET1;
    float4 t2 : SV_TARGET2;
    float4 t3 : SV_TARGET3;
};
PSOutput main(PSInput input) {
    float4 r[48]; float4 h[48];
    [unroll] for (int _i = 0; _i < 48; _i++) { r[_i] = (float4)0; h[_i] = (float4)0; }
    float4 cc0 = (float4)0; float4 cc1 = (float4)0;
    { float4 _v = (float4)(rsx_tex[3].SampleLevel(rsx_samp[3], ((input.tc1).zwzz).xy, ((float4(0,0,0,0)).xxxx).x)); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).wwww) + ((float4(-9.99,0.999,-0.1001,-0.1)).yyyy)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((input.tc1).zwzz).xy)); r[3].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((float4(-1,0,0,0)).xxxx)); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[3]).xxxx) >  (-((r[3]).yyyy)))); h[0].z = _v.z; }
    { float4 _v = (float4)((-((float4(-9.99,0.999,-0.1001,-0.1)).xxxx)) / ((r[0]).xyzw).x); r[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz); r[2].x = _v.x; }
    { float4 _v = (float4)((r[0]).wwww); r[0].x = _v.x; }
    { float4 _v = (float4)((float4)(((r[0]).xyzw) <  ((float4(14,0,0,0)).xxxx))); h[1].w = _v.w; }
    { float4 _v = (float4)((float4)(((h[0]).zzzz) == ((float4(0,0,0,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((r[3]).zzzz);
      cc0.x = _v.x;
    }
    { float4 _v = (float4)(((h[0]).xyzw) * ((h[1]).xyzw));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)((-((r[3]).wwww)) + ((float4(1,0,0,0)).xxxx)); r[2].y = _v.y; }
    { float4 _v = (float4)((float4(65504,0,0,0)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      r[0].x = (_p.x != 0.0) ? _v.x : r[0].x;
    }
    { float4 _v = (float4)((input.tc0).xxxy); r[0].zw = _v.zw; }
    { float4 _v = (float4)((h[0]).zzzz);
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[0]).xxxx)); r[3].z = _v.z; }
    { float4 _v = (float4)(((r[3]).zzzz) * ((float4(0,1,0,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).zzzz) * ((r[0]).xxxx)); r[1].w = _v.w; }
    { float4 _v = (float4)(((r[1]).wwww) * ((float4(1,0,0,0)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xxxx) * ((float4(0,0,0.999,1)).xywz) + ((r[1]).xyzw)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) + ((float4(0,0,-9.99,0)).xywz)); r[1].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[1]).xyzw) / ((r[1]).zzzz).x); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].w = (_p.w != 0.0) ? _v.w : r[4].w;
    }
    { float4 _v = (float4)(((r[0]).zwzz) + (-((r[0]).xyzw))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[3]).xxxy) * ((float4(2,-1,0,0)).xxxx) + ((float4(2,-1,0,0)).yyyy)); h[1].zw = _v.zw; }
    { float4 _v = (float4)(((r[0]).xxxy) * ((float4(38.6317,-21.7303,0,0)).xxxy));
      float4 _p = (float4)((cc0).wwww == (float4)0.0);
      h[1].zw = (_p.zw != 0.0) ? _v.zw : h[1].zw;
    }
    { float4 _v = (float4)((float4(0,0,0,0)).zzzz); h[0].xy = _v.xy; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)) * 2.0; r[4].xy = _v.xy; }
    { float4 _v = (float4)(dot(((h[1]).zwzz).xy, ((h[1]).zwzz).xy)); h[1].x = _v.x; }
    { float4 _v = (float4)((float4)(((h[1]).xxxx) >  ((float4(1,0,0,0)).xxxx)));
      cc0.y = _v.y;
    }
    { float4 _v = (float4)((input.tc1).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)((h[1]).xyzw); h[0].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) + (-((float4(0.0125,0.0222222,0.1,0.05625)).zwzz)));
      float4 _p = (float4)((cc0).xxxx > (float4)0.0);
      h[0].xy = (_p.xy != 0.0) ? _v.xy : h[0].xy;
    }
    { float4 _v = (float4)((abs((h[1]).xyzw) > 0.0 ? ((h[1]).xyzw) / sqrt(abs(((h[1]).xyzw).x)) : (float4)0.0));
      float4 _p = (float4)((cc0).yyyy != (float4)0.0);
      h[0].zw = (_p.zw != 0.0) ? _v.zw : h[0].zw;
    }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xy = _v.xy; }
    { float4 _v = (float4)(((h[0]).zwzz) * ((float4(0.0125,0.0222222,0.1,0.05625)).xyxx) + ((h[0]).xyzw)); r[4].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[4]).wwww) + ((r[1]).xyzw)); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx); r[1].x = _v.x; }
    { float4 _v = (float4)((float4(-0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].x = (_p.x != 0.0) ? _v.x : r[1].x;
    }
    { float4 _v = (float4)(min(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((r[4]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[1]).xxxx) + ((r[1]).zwzz)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.6,0,0,1)).xxxx); r[2].w = _v.w; }
    { float4 _v = (float4)(min(((r[1]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[2].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[2].w = (_p.w != 0.0) ? _v.w : r[2].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[5].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[2]).xxxy), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[4].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((r[1]).xyzw); r[1].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[4]).zwzz).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((r[2]).wwww) + ((r[1]).xyzw)); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)((-((r[3]).xyzw)) + ((r[1]).xyzw)); h[3].xy = _v.xy; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((h[3]).xyzw).xy, ((h[3]).xyzw).xy)); r[2].x = _v.x; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[1].w = (_p.w != 0.0) ? _v.w : r[1].w;
    }
    { float4 _v = (float4)((-((r[2]).xyzw)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].x = _v.x; }
    { float4 _v = (float4)(dot(((h[5]).xyzw).xy, ((h[5]).xyzw).xy)); r[1].x = _v.x; }
    { float4 _v = (float4)((-((r[1]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[2].w = _v.w; }
    { float4 _v = (float4)((r[2]).xyzw); r[2].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[0]).wwww)); r[5].x = _v.x; }
    { float4 _v = (float4)(((r[2]).xyzw) * ((r[1]).xyzw)); r[2].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].w = (_p.w != 0.0) ? _v.w : r[0].w;
    }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[0].Sample(rsx_samp[0], ((input.tc1).zwzz).xy)); r[1].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[1]).xyzw) * ((r[0]).wwww) + ((r[0]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)((float4)((abs((r[1]).xyzw)) <  ((float4(0,0.0005,4,0)).xxxx)));
      cc0.w = _v.w;
    }
    { float4 _v = (float4)(min(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyzw))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[5].y = _v.y; }
    { float4 _v = (float4)(((r[0]).wwww) + ((r[2]).wwww)); h[11].x = _v.x; }
    { float4 _v = (float4)(max(((r[3]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xxxy))); r[3].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[5].y = (_p.y != 0.0) ? _v.y : r[5].y;
    }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[4]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).xxxx) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[5]).xxxx) + ((h[11]).xxxx)); h[9].w = _v.w; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[3]).zwzz).xy)); r[0].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[0]).xxxy)); h[11].zw = _v.zw; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[3]).zwzz).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(dot(((h[11]).zwzz).xy, ((h[11]).zwzz).xy)); r[5].x = _v.x; }
    { float4 _v = (float4)((-((r[5]).xxxx)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[0].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[5]).yyyy)); r[2].w = _v.w; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[2]).wwww) + ((r[2]).xyzw)); r[2].xyz = _v.xyz; }
    { float4 _v = (float4)(rsx_tex[1].Sample(rsx_samp[1], ((input.tc0).zwzz).xy)); r[0].xyzw = _v.xyzw; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((float4(4,0,0,0)).xxxx)); h[7].xyzw = _v.xyzw; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).yyyy); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[2]).wwww) + ((h[9]).wwww)); h[5].z = _v.z; }
    { float4 _v = (float4)((abs((r[1]).xyzw)) + (-((float4(0,0.0005,4,0)).xxxx))); h[0].w = _v.w; }
    { float4 _v = (float4)((abs((h[0]).wwww)) * ((float4(0,0.0005,4,0)).yyyy)); _v = saturate(_v); h[9].x = _v.x; }
    { float4 _v = (float4)(log2(((h[9]).xyzw).x)); h[9].x = _v.x; }
    { float4 _v = (float4)((float4(0,0,0.00078125,0.00138889)).xxxx);
      float4 _p = (float4)((cc0).wwww != (float4)0.0);
      h[0].x = (_p.x != 0.0) ? _v.x : h[0].x;
    }
    { float4 _v = (float4)(((h[9]).xxxx) * ((float4(0,0.0005,4,0)).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(exp2(((h[0]).wwww).x)); h[0].y = _v.y; }
    { float4 _v = (float4)(min(((h[0]).xyzw), ((h[0]).yyyy))); h[0].x = _v.x; }
    { float4 _v = (float4)(((r[4]).xxxy) * ((float4(80,45,0,0)).xxxy)); r[4].zw = _v.zw; }
    { float4 _v = (float4)(max(((h[0]).xyzw), ((float4(0,0.0005,4,0)).wwww))); h[1].x = _v.x; }
    { float4 _v = (float4)((-((h[1]).xxxx)) + ((float4(0,1,0,0)).yyyy)); r[0].w = _v.w; }
    { float4 _v = (float4)((float4(0.8,0,0,1)).xxxx); r[0].z = _v.z; }
    { float4 _v = (float4)(((r[0]).wwww) * ((r[1]).xyzw) + ((h[7]).xyzw)); h[3].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) + ((h[7]).xyzw)); h[3].w = _v.w; }
    { float4 _v = (float4)((input.tc1).zwzz); r[0].xy = _v.xy; }
    { float4 _v = (float4)((float4(-0.4,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[0].z = (_p.z != 0.0) ? _v.z : r[0].z;
    }
    { float4 _v = (float4)(((r[4]).xyzw) * ((r[0]).zzzz) + ((r[0]).xyzw)); r[0].xy = _v.xy; }
    { float4 _v = (float4)(min(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).zwzz))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(max(((r[0]).xyzw), ((float4(0.00078125,0.00138889,0.999219,0.998611)).xyxx))); r[0].xy = _v.xy; }
    { float4 _v = (float4)(rsx_tex[2].Sample(rsx_samp[2], ((r[0]).xyzw).xy)); r[1].xy = _v.xy; }
    { float4 _v = (float4)((-((r[3]).xxxy)) + ((r[1]).xxxy)); h[2].zw = _v.zw; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx); r[4].x = _v.x; }
    { float4 _v = (float4)(rsx_tex[4].Sample(rsx_samp[4], ((r[0]).xyzw).xy)); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)((float4(0.2,0,0,1)).xxxx);
      float4 _p = (float4)((cc0).xxxx <= (float4)0.0);
      r[4].x = (_p.x != 0.0) ? _v.x : r[4].x;
    }
    { float4 _v = (float4)(dot(((h[2]).zwzz).xy, ((h[2]).zwzz).xy)); r[4].y = _v.y; }
    { float4 _v = (float4)(((h[3]).xyzw) / ((h[3]).wwww).x); h[2].xyz = _v.xyz; }
    { float4 _v = (float4)((-((r[4]).yyyy)) * ((float4(10,1,0,0)).xxxx) + ((float4(10,1,0,0)).yyyy)); _v = saturate(_v); r[1].w = _v.w; }
    { float4 _v = (float4)(dot(((r[4]).zwzz).xy, ((r[4]).zwzz).xy)); r[1].z = _v.z; }
    { float4 _v = (float4)(((r[1]).wwww) * ((r[4]).xyzw)); r[3].x = _v.x; }
    { float4 _v = (float4)((abs(abs((r[1]).zzzz)) > 0.0 ? (abs((r[1]).zzzz)) / sqrt(abs(((r[1]).zzzz).x)) : (float4)0.0)); _v = saturate(_v); h[5].w = _v.w; }
    { float4 _v = (float4)(((h[5]).xyzw) * ((r[0]).xyzw)); h[2].w = _v.w; }
    { float4 _v = (float4)((-((h[2]).xyzw)) * ((r[0]).xyzw) + ((r[0]).xyzw)); r[0].w = _v.w; }
    { float4 _v = (float4)((r[0]).xyzw); r[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[0]).xyzw) * ((r[3]).xxxx) + ((r[2]).xyzw)); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((r[3]).xxxx) + ((h[5]).zzzz)); h[0].w = _v.w; }
    { float4 _v = (float4)(((h[0]).xyzw) / ((h[0]).wwww).x); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[0]).xyzw) + (-((h[2]).xyzw))); h[0].xyz = _v.xyz; }
    { float4 _v = (float4)(((h[2]).wwww) * ((h[0]).xyzw) + ((h[2]).xyzw)) / 4.0; r[0].xyz = _v.xyz; }
    PSOutput _out;
    float4 _o0 = r[0];
    _out.t0 = (_o0 == _o0) ? _o0 : (float4)0;
    float4 _o1 = r[2];
    _out.t1 = (_o1 == _o1) ? _o1 : (float4)0;
    float4 _o2 = r[3];
    _out.t2 = (_o2 == _o2) ? _o2 : (float4)0;
    float4 _o3 = r[4];
    _out.t3 = (_o3 == _o3) ? _o3 : (float4)0;
    return _out;
}

