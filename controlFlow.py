def BZ(self, RS, Address):
    if RS == 0:
        self.PC = Address
        self.flush()
    return

def BEQ(self, RS, RT, Address):
    if RS == RT:
        self.PC = Address
        self.flush()
    return

def JR(self,RS):
    jumpTo = RS >> 2
    self.PC = jumpTo
    self.flush()
    return