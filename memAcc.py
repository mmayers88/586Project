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

# Example for STW

b = 12
address_b = id(b)
print (address_b)
memfield = (ctypes.c_int).from_address(address_b)
print(memfield)