from ctypes import Structure, c_char_p, c_uint, c_byte, c_float, c_int, c_ubyte, c_bool, POINTER, WINFUNCTYPE
from enum import IntEnum, IntFlag
from Enum_Common import EnumField
from D3D11_constants import D3D11_SIMULTANEOUS_RENDER_TARGET_COUNT
from COM.DeviceChild import ID3D11DeviceChildVtbl as ID3D11DeviceChild
from COM.Common import *
from COM.GUID import *
from DXGI.IDL.Format import DXGI_FORMAT
from Draw import D3D11_USAGE
from Resources import ID3D11ResourceVtbl as ID3D11Resource

class D3D11_TEXTURE1D_DESC(Structure):
	_fields_ = [
		("Width", c_uint),
		("MipLevels", c_uint),
		("ArraySize", c_uint),
		("Format", c_int),
		("Usage", c_int),
		("BindFlags", c_uint),
		("CPUAccessFlags", c_uint),
		("MiscFlags", c_uint),
	]

class ID3D11Texture1DVtbl(ID3D11Resource):
    _fields_ = ID3D11Resource._fields_ + [
        ("GetDesc", WINFUNCTYPE(None, c_void_p, POINTER(D3D11_TEXTURE1D_DESC))),
    ]


class ID3D11Texture1D(Structure):
    IID = MS_UUID("f8fb5c27-c6b3-4f75-a4c8-439af2ef564c")
    _fields_ = [("lpVtbl", POINTER(ID3D11Texture1DVtbl))]


