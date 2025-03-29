from ctypes import Structure, c_char_p, c_uint, c_byte, c_float, c_int, c_ubyte, c_bool, POINTER, WINFUNCTYPE
from enum import IntEnum, IntFlag
from Enum_Common import EnumField
from D3D11_constants import D3D11_SIMULTANEOUS_RENDER_TARGET_COUNT
from COM.DeviceChild import ID3D11DeviceChildVtbl as ID3D11DeviceChild
from COM.Common import *
from COM.GUID import *
from Draw import D3D11_USAGE
from Resources import ID3D11ResourceVtbl as ID3D11Resource

class D3D11_BUFFER_DESC(Structure):
	_fields_ = [
		("ByteWidth", c_uint),
		("Usage", c_int),
		("BindFlags", c_uint),
		("CPUAccessFlags", c_uint),
		("MiscFlags", c_uint),
		("StructureByteStride", c_uint)
	]
	Usage = EnumField("Usage", D3D11_USAGE)


class ID3D11BufferVtbl(ID3D11DeviceChild):
    _fields_ = ID3D11DeviceChild._fields_ + [
        ("GetDesc", WINFUNCTYPE(None, c_void_p, POINTER(D3D11_BUFFER_DESC))),
    ]

class ID3D11Buffer(Structure):
    IID = MS_UUID("48570b85-d1ee-4fcd-a250-eb350722b037")
    _fields_ = [("lpVtbl", POINTER(ID3D11BufferVtbl))]


