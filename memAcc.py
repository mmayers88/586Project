import ctypes

def LDW(RS, IMM):
    Address = RS + IMM
    Answer = ctypes.cast(Address, ctypes.py_object).value
    return Answer

def STW(RS, IMM):
    Address = RS + IMM
    #Answer =
    return Answer



# Example for LDW
# a = 5
# address = id(a)
# cast_value = ctypes.cast(address, ctypes.py_object).value
# print(cast_value)
