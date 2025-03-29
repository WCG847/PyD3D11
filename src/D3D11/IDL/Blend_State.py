from ctypes import Structure, c_char_p, c_uint, c_byte, c_float, c_int, c_ubyte, c_bool, POINTER, WINFUNCTYPE
from enum import IntEnum, IntFlag
from Enum_Common import EnumField
from D3D11_constants import D3D11_SIMULTANEOUS_RENDER_TARGET_COUNT
from COM.DeviceChild import ID3D11DeviceChildVtbl as ID3D11DeviceChild
from COM.Common import *
from COM.GUID import *


class D3D11_BLEND(IntEnum):
	D3D11_BLEND_ZERO = 1
	D3D11_BLEND_ONE = 2
	D3D11_BLEND_SRC_COLOR = 3
	D3D11_BLEND_INV_SRC_COLOR = 4
	D3D11_BLEND_SRC_ALPHA = 5
	D3D11_BLEND_INV_SRC_ALPHA = 6
	D3D11_BLEND_DEST_ALPHA = 7
	D3D11_BLEND_INV_DEST_ALPHA = 8
	D3D11_BLEND_DEST_COLOR = 9
	D3D11_BLEND_INV_DEST_COLOR = 10
	D3D11_BLEND_SRC_ALPHA_SAT = 11
	D3D11_BLEND_BLEND_FACTOR = 14
	D3D11_BLEND_INV_BLEND_FACTOR = 15
	D3D11_BLEND_SRC1_COLOR = 16
	D3D11_BLEND_INV_SRC1_COLOR = 17
	D3D11_BLEND_SRC1_ALPHA = 18
	D3D11_BLEND_INV_SRC1_ALPHA = 19

class D3D11_BLEND_OP(IntEnum):
	D3D11_BLEND_OP_ADD = 1
	D3D11_BLEND_OP_SUBTRACT = 2
	D3D11_BLEND_OP_REV_SUBTRACT = 3
	D3D11_BLEND_OP_MIN = 4
	D3D11_BLEND_OP_MAX = 5

class D3D11_COLOR_WRITE_ENABLE(IntEnum):
	D3D11_COLOR_WRITE_ENABLE_RED = 1
	D3D11_COLOR_WRITE_ENABLE_GREEN = 2
	D3D11_COLOR_WRITE_ENABLE_BLUE = 4
	D3D11_COLOR_WRITE_ENABLE_ALPHA = 8
	D3D11_COLOR_WRITE_ENABLE_ALL = (D3D11_COLOR_WRITE_ENABLE_RED|D3D11_COLOR_WRITE_ENABLE_GREEN|
		D3D11_COLOR_WRITE_ENABLE_BLUE|D3D11_COLOR_WRITE_ENABLE_ALPHA)

class D3D11_RENDER_TARGET_BLEND_DESC(Structure):
	_fields_ = [
		("BlendEnable", c_bool),
		("SrcBlend", c_int),
		("DestBlend", c_int),
		("BlendOp", c_int),
		("SrcBlendAlpha", c_int),
		("DestBlendAlpha", c_int),
		("BlendOpAlpha", c_int),
		("RenderTargetWriteMask", c_ubyte)
		]
	SrcBlend = EnumField("SrcBlend", D3D11_BLEND)
	DestBlend = EnumField("DestBlend", D3D11_BLEND)
	BlendOp = EnumField("BlendOp", D3D11_BLEND_OP)
	SrcBlendAlpha = EnumField("SrcBlendAlpha", D3D11_BLEND)
	DestBlendAlpha = EnumField("DestBlendAlpha", D3D11_BLEND)
	BlendOpAlpha = EnumField("BlendOpAlpha", D3D11_BLEND_OP)

class D3D11_BLEND_DESC(Structure):
    _fields_ = [
        ("AlphaToCoverageEnable", c_bool),
        ("IndependentBlendEnable", c_bool),
        ("RenderTarget", D3D11_RENDER_TARGET_BLEND_DESC * D3D11_SIMULTANEOUS_RENDER_TARGET_COUNT),
    ]


class ID3D11BlendStateVtbl(ID3D11DeviceChild):
    _fields_ = ID3D11DeviceChild._fields_ + [
        ("GetDesc", WINFUNCTYPE(None, c_void_p, POINTER(D3D11_BLEND_DESC))),
    ]

class ID3D11BlendState(Structure):
    IID = MS_UUID("75b68faa-347d-4159-8f45-a0640f01cd9a")
    _fields_ = [("lpVtbl", POINTER(ID3D11BlendStateVtbl))]










