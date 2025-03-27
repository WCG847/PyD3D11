from ctypes import Structure, POINTER, WINFUNCTYPE, c_void_p, c_uint, c_ulong, c_int, c_long
from GUID import *
from Common import *

class ID3D11DeviceChildVtbl(IUnknownVtbl):
    _fields_ = IUnknownVtbl._fields_ + [
        ("GetDevice", WINFUNCTYPE(None, c_void_p, POINTER(POINTER(ID3D11Device)))),  # ID3D11Device**
        ("GetPrivateData", WINFUNCTYPE(HRESULT, c_void_p, REFGUID, POINTER(c_uint), c_void_p)),
        ("SetPrivateData", WINFUNCTYPE(HRESULT, c_void_p, REFGUID, c_uint, c_void_p)),
        ("SetPrivateDataInterface", WINFUNCTYPE(HRESULT, c_void_p, REFGUID, c_void_p)),
    ]

class ID3D11DeviceChild(Structure):
    IID = MS_UUID("1841e5c8-16b0-489b-bcc8-44cfb0d5deae")
    _fields_ = [("lpVtbl", POINTER(ID3D11DeviceChildVtbl))]
