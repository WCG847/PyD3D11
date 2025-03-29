
from ctypes import Structure, c_char_p, c_uint
from enum import IntEnum

class D3D11_INPUT_CLASSIFICATION(IntEnum):
	D3D11_INPUT_PER_VERTEX_DATA = 0
	D3D11_INPUT_PER_INSTANCE_DATA = 1

class D3D11_INPUT_ELEMENT_DESC(Structure):
	_fields_ = [
		("SemanticName", c_char_p), 
		("SemanticIndex", c_uint), 
		("Format", c_uint),         
		("InputSlot", c_uint),       
		("AlignedByteOffset", c_uint),
		("InputSlotClass", c_uint), 
		("InstanceDataStepRate", c_uint),
	]