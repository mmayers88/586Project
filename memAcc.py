import ctypes

def LDW(RS, IMM):
    RS = int(RS, 2)
    if IMM[0] == 1:
        IMM = int(IMM, 2)
        IMM = -1 * IMM
    else:
        IMM = int(IMM, 2)
    Address = RS + IMM
    #Answer = ctypes.cast(Address, ctypes.py_object).value
    Answer = '{0:032b}'.format(Answer)
    return Answer

def STW(RS, IMM):
    RS = int(RS, 2)
    if IMM[0] == 1:
        IMM = int(IMM, 2)
        IMM = -1 * IMM
    else:
        IMM = int(IMM, 2)
    Address = RS + IMM
    #Answer = ctypes.cast(Address, ctypes.py_object).value
    Answer = '{0:032b}'.format(Answer)
    return Answer


