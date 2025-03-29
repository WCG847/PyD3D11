from ctypes import (    Structure,    c_bool,    c_char_p,    c_uint,    c_byte,    c_float,    c_int,    c_bool,    c_ubyte,    POINTER,    WINFUNCTYPE,    c_void_p,    c_uint,    c_ulong,    c_int,    c_long,)
from enum import IntEnum, IntFlag
from COM.Common import *
from COM.GUID import *
from COM.DeviceChild import *


class D3D11_COMPARISON_FUNC(IntEnum):
    D3D11_COMPARISON_NEVER = 1
    D3D11_COMPARISON_LESS = 2
    D3D11_COMPARISON_EQUAL = 3
    D3D11_COMPARISON_LESS_EQUAL = 4
    D3D11_COMPARISON_GREATER = 5
    D3D11_COMPARISON_NOT_EQUAL = 6
    D3D11_COMPARISON_GREATER_EQUAL = 7
    D3D11_COMPARISON_ALWAYS = 8


class D3D11_DEPTH_WRITE_MASK(IntEnum):
    D3D11_DEPTH_WRITE_MASK_ZERO = 0
    D3D11_DEPTH_WRITE_MASK_ALL = 1


class D3D11_STENCIL_OP(IntEnum):
    D3D11_STENCIL_OP_KEEP = 1
    D3D11_STENCIL_OP_ZERO = 2
    D3D11_STENCIL_OP_REPLACE = 3
    D3D11_STENCIL_OP_INCR_SAT = 4
    D3D11_STENCIL_OP_DECR_SAT = 5
    D3D11_STENCIL_OP_INVERT = 6
    D3D11_STENCIL_OP_INCR = 7
    D3D11_STENCIL_OP_DECR = 8


class D3D11_DEPTH_STENCILOP_DESC(Structure):
    _fields_ = [
        ("_StencilFailOp", c_int),
        ("_StencilDepthFailOp", c_int),
        ("_StencilPassOp", c_int),
        ("_StencilFunc", c_int),
    ]

    @property
    def StencilFailOp(self):
        return D3D11_STENCIL_OP(self._StencilFailOp)

    @StencilFailOp.setter
    def StencilFailOp(self, val):
        self._StencilFailOp = int(val)

    @property
    def StencilDepthFailOp(self):
        return D3D11_STENCIL_OP(self._StencilDepthFailOp)

    @StencilDepthFailOp.setter
    def StencilDepthFailOp(self, val):
        self._StencilDepthFailOp = int(val)

    @property
    def StencilPassOp(self):
        return D3D11_STENCIL_OP(self._StencilPassOp)

    @StencilPassOp.setter
    def StencilPassOp(self, val):
        self._StencilPassOp = int(val)

    @property
    def StencilFunc(self):
        return D3D11_COMPARISON_FUNC(self._StencilFunc)

    @StencilFunc.setter
    def StencilFunc(self, val):
        self._StencilFunc = int(val)


class D3D11_DEPTH_STENCIL_DESC(Structure):
    _fields_ = [
        ("DepthEnable", c_bool),
        ("DepthWriteMask", c_int),
        ("DepthFunc", c_int),
        ("StencilEnable", c_bool),
        ("StencilReadMask", c_ubyte),
        ("FrontFace", c_int),
        ("BackFace", c_int),
    ]

    @property
    def DepthWriteMask(self):
        return D3D11_DEPTH_WRITE_MASK(self._DepthWriteMask)

    @DepthWriteMask.setter
    def DepthWriteMask(self, val):
        self._DepthWriteMask = int(val)

    @property
    def DepthFunc(self):
        return D3D11_COMPARISON_FUNC(self._DepthFunc)

    @DepthFunc.setter
    def DepthFunc(self, val):
        self._DepthFunc = int(val)

    @property
    def FrontFace(self):
        return D3D11_DEPTH_STENCILOP_DESC(self._FrontFace)

    @FrontFace.setter
    def FrontFace(self, val):
        self._FrontFace = int(val)

    @property
    def BackFace(self):
        return D3D11_DEPTH_STENCILOP_DESC(self._BackFace)

    @BackFace.setter
    def BackFace(self, val):
        self._BackFace = int(val)


class ID3D11DepthStencilStateVtbl(ID3D11DeviceChildVtbl):
    _fields_ = ID3D11DeviceChildVtbl._fields_ + [
        ("GetDesc", WINFUNCTYPE(None, c_void_p, POINTER(D3D11_DEPTH_STENCIL_DESC))),
    ]


class ID3D11DepthStencilState(Structure):
    IID = MS_UUID("03823efb-8d8f-4e1c-9aa2-f64bb2cbfdf1")
    _fields_ = [("lpVtbl", POINTER(ID3D11DepthStencilStateVtbl))]
