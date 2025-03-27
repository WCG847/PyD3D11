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

class IUnknown(Structure):
    _fields_ = [("lpVtbl", POINTER(IUnknownVtbl))]

    def QueryInterface(self, riid, ppvObject):
        return self.lpVtbl.contents.QueryInterface(self, riid, ppvObject)

    def AddRef(self):
        return self.lpVtbl.contents.AddRef(self)

    def Release(self):
        return self.lpVtbl.contents.Release(self)
