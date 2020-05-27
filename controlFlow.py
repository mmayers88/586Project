'''
question: are we jumping to that line or is that the address?
    if IMM == 100:
        am I jumping to PC +100 or PC + IMM>>2 or PC - 2 + IMM>>2 or PC - 2 + IMM?
    I assume it's PC -2 + IMM
        I subtract 2 because the PC was at that number when fetched.

JR:
    following the instruction literally take us to a weird place in memory
'''

def BZ(self, RS, Address):
    print("RS: ", RS)
    if RS == 0:
        self.PC = self.PC - 2 + Address
        self.flush()
    return

def BEQ(self, RS, RT, Address):
    print("RS: ",RS)
    print("RT: ", RT)
    if RS == RT:
        self.PC = self.PC - 2 + Address
        self.flush()
    return

def JR(self,RS):
    jumpTo = RS >> 2
    self.PC = jumpTo
    self.flush()
    return



#this happens in init
self.fileName = open(self.fileWord, 'r')
self.memory = self.fileName.readlines()

#this happens when storing
self.memory[1] = "Line2\n"
self.fileName = open(self.fileWord, 'w')
self.fileName.writelines(self.memory)
self.fileName.close()

self.fileName = open(self.fileWord, 'r')
self.memory = self.fileName.readlines()

