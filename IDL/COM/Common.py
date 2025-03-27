from ctypes import Structure, POINTER, WINFUNCTYPE, c_void_p, c_uint, c_ulong, c_int, c_long
from GUID import *

HRESULT = c_long
REFGUID = POINTER(GUID)

class IUnknownVtbl(Structure):
    _fields_ = [
        ("QueryInterface", WINFUNCTYPE(HRESULT, c_void_p, REFGUID, POINTER(c_void_p))),
        ("AddRef", WINFUNCTYPE(c_ulong, c_void_p)),
        ("Release", WINFUNCTYPE(c_ulong, c_void_p)),
    ]
