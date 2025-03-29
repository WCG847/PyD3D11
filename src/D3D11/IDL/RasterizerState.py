from ctypes import Structure, c_char_p, c_uint, c_byte, c_float, c_int, c_ubyte, c_bool, POINTER, WINFUNCTYPE
from enum import IntEnum, IntFlag
from Enum_Common import EnumField
from D3D11_constants import D3D11_SIMULTANEOUS_RENDER_TARGET_COUNT
from COM.DeviceChild import ID3D11DeviceChildVtbl as ID3D11DeviceChild
from COM.Common import *
from COM.GUID import *
from Draw import D3D11_CULL_MODE, D3D11_FILL_MODE

class D3D11_RASTERIZER_DESC(Structure):
	_fields_ = [
		("FillMode", c_int),
		("CullMode", c_int),
		("FrontCounterClockwise", c_bool),
		("DepthBias", c_int),
		("DepthBiasClamp", c_float),
		("SlopeScaledDepthBias", c_float),
		("DepthClipEnable", c_bool),
		("ScissorEnable", c_bool),
		("MultisampleEnable", c_bool),
		("AntialiasedLineEnable", c_bool)
	]

	FillMode = EnumField("FillMode", D3D11_FILL_MODE)
	CullMode = EnumField("CullMode", D3D11_CULL_MODE)



class ID3D11RasterizerStateVtbl(ID3D11DeviceChild):
    _fields_ = ID3D11DeviceChild._fields_ + [
        ("GetDesc", WINFUNCTYPE(None, c_void_p, POINTER(D3D11_RASTERIZER_DESC))),
    ]

class ID3D11RasterizerState(Structure):
    IID = MS_UUID("9bb4ab81-ab1a-4d8f-b506-fc04200b6ee7")
    _fields_ = [("lpVtbl", POINTER(ID3D11RasterizerStateVtbl))]







