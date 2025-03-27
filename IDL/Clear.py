from ctypes import Structure, c_char_p, c_uint, c_byte, c_float, c_int
from enum import IntEnum, IntFlag

# Flags for ClearDepthStencil
class D3D11_CLEAR_FLAG(IntFlag):
	D3D11_CLEAR_DEPTH = 0x01
	D3D11_CLEAR_STENCIL = 0x02