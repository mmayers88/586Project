def OR(self, RS, RT):
    RS = int(RS, 2)
    RT = int(RT, 2)
    Answer = RS | RT
    return Answer


def ORI(self, RS, IMM):
    RS = int(RS, 2)
    IMM = int(IMM, 2)
    Answer = RS | IMM
    return Answer


def AND(self, RS, RT):
    RS = int(RS, 2)
    RT = int(RT, 2)
    Answer = RS & RT
    return Answer


def ANDI(self, RS, IMM):
    RS = int(RS, 2)
    IMM = int(IMM, 2)
    Answer = RS & IMM
    return Answer


def XOR(self, RS, RT):
    RS = int(RS, 2)
    RT = int(RT, 2)
    Answer = RS ^ RT
    return Answer


def XORI(self, RS, IMM):
    RS = int(RS, 2)
    IMM = int(IMM, 2)
    Answer = RS ^IMM
    return Answer



