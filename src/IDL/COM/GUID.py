from ctypes import Structure, c_ulong, c_ushort, c_ubyte

class GUID(Structure):
    _fields_ = [
        ("Data1", c_ulong),
        ("Data2", c_ushort),
        ("Data3", c_ushort),
        ("Data4", c_ubyte * 8),
    ]

import uuid

def MS_UUID(s: str) -> GUID:
    u = uuid.UUID(s)
    return GUID(
        u.time_low,
        u.time_mid,
        u.time_hi_version,
        (u.clock_seq_hi_variant, u.clock_seq_low) + tuple(u.node.to_bytes(6, 'big'))
    )
