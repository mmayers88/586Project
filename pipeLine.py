import queue
class pipeline:
    def __init__(self):
        self.PC = 0

    #instruction fetch
    def IF(self):
        return

    #instruction decode
    def ID(self):
        return

    #execute Instruction
    def EX(self):
        return

    #memory
    #load or store from or to memory
    def MEM(self):
        return

    #write back instruction
    #write back to register
    def WB(self):
        return


    def iORrORn(self):
        #6 MSB are the opcode
        return

    def JR(self,address):
        jumpTo = address >> 5
        return jumpTo

    #this will be the "main" function basically
    def cycle(self):
        return
