from ctypes import Structure, c_char_p, c_uint, c_byte, c_float, c_int, c_ubyte, c_bool, POINTER, WINFUNCTYPE
from enum import IntEnum, IntFlag
from Enum_Common import EnumField
from D3D11_constants import D3D11_SIMULTANEOUS_RENDER_TARGET_COUNT
from COM.DeviceChild import ID3D11DeviceChildVtbl as ID3D11DeviceChild
from COM.Common import *
from COM.GUID import *
from Draw import D3D11_RESOURCE_DIMENSION

class D3D11_RESOURCE_MISC_FLAG(IntFlag):
	D3D11_RESOURCE_MISC_GENERATE_MIPS                   = 0x00000001
	D3D11_RESOURCE_MISC_SHARED                          = 0x00000002
	D3D11_RESOURCE_MISC_TEXTURECUBE                     = 0x00000004
	D3D11_RESOURCE_MISC_DRAWINDIRECT_ARGS               = 0x00000010
	D3D11_RESOURCE_MISC_BUFFER_ALLOW_RAW_VIEWS          = 0x00000020
	D3D11_RESOURCE_MISC_BUFFER_STRUCTURED               = 0x00000040
	D3D11_RESOURCE_MISC_RESOURCE_CLAMP                  = 0x00000080
	D3D11_RESOURCE_MISC_SHARED_KEYEDMUTEX               = 0x00000100
	D3D11_RESOURCE_MISC_GDI_COMPATIBLE                  = 0x00000200
	D3D11_RESOURCE_MISC_SHARED_NTHANDLE                 = 0x00000800
	D3D11_RESOURCE_MISC_RESTRICTED_CONTENT              = 0x00001000
	D3D11_RESOURCE_MISC_RESTRICT_SHARED_RESOURCE        = 0x00002000
	D3D11_RESOURCE_MISC_RESTRICT_SHARED_RESOURCE_DRIVER = 0x00004000
	D3D11_RESOURCE_MISC_GUARDED                         = 0x00008000
	D3D11_RESOURCE_MISC_TILE_POOL                       = 0x00020000
	D3D11_RESOURCE_MISC_TILED                           = 0x00040000
	D3D11_RESOURCE_MISC_HW_PROTECTED                    = 0x00080000
	D3D11_RESOURCE_MISC_SHARED_DISPLAYABLE              = 0x00100000
	D3D11_RESOURCE_MISC_SHARED_EXCLUSIVE_WRITER         = 0x00200000


class D3D11_SUBRESOURCE_DATA(Structure):
    _fields_ = [
        ("pSysMem", c_void_p),      
        ("SysMemPitch", c_uint),     
        ("SysMemSlicePitch", c_uint) 
    ]

class D3D11_MAPPED_SUBRESOURCE(Structure):
    _fields_ = [
        ("pData", c_void_p),
        ("RowPitch", c_uint),
        ("DepthPitch", c_uint),
    ]

class ID3D11ResourceVtbl(ID3D11DeviceChild):
    _fields_ = ID3D11DeviceChild._fields_ + [
        ("GetType", WINFUNCTYPE(None, c_void_p, POINTER(D3D11_RESOURCE_DIMENSION))),
        ("SetEvictionPriority", WINFUNCTYPE(None, c_void_p, c_uint)),
        ("GetEvictionPriority", WINFUNCTYPE(c_uint, c_void_p)),
    ]

class ID3D11Resource(Structure):
    IID = MS_UUID("dc8e63f3-d12b-4952-b47b-5e45026a862d")
    _fields_ = [("lpVtbl", POINTER(ID3D11ResourceVtbl))]

