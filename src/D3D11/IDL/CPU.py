from ctypes import Structure, c_char_p, c_uint, c_byte, c_float, c_int
from enum import IntEnum, IntFlag

class D3D11_CPU_ACCESS_FLAG(IntFlag):
	D3D11_CPU_ACCESS_WRITE = 0x00010000
	D3D11_CPU_ACCESS_READ = 0x00020000

