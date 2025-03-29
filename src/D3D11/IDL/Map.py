from ctypes import Structure, c_char_p, c_uint, c_byte, c_float, c_int
from enum import IntEnum, IntFlag

class D3D11_MAP(IntEnum):
	D3D11_MAP_READ = 1
	D3D11_MAP_WRITE = 2
	D3D11_MAP_READ_WRITE = 3
	D3D11_MAP_WRITE_DISCARD = 4
	D3D11_MAP_WRITE_NO_OVERWRITE = 5

class D3D11_MAP_FLAG(IntFlag):
	D3D11_MAP_FLAG_DO_NOT_WAIT = 0x00100000

