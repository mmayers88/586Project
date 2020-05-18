
class CPU:
    pipeline = {1:'x', 2: 'x', 3: 'x', 4: 'x', 5: 'x'}
    PC = 0
    def __init__(self):
        self.pipeline[1]='1'
        return      

    def printData(self):
        print(self.pipeline)
        print(self.PC)
        return

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
        #IF
        #ID
        #EX
        #MEM
        #WB
        
        #increment pipeline
        self.pipeline[5] = self.pipeline[4]
        self.pipeline[4] = self.pipeline[3]
        self.pipeline[3] = self.pipeline[4]
        self.pipeline[2] = self.pipeline[1]
        self.pipeline[1] = 'x'
        return


def main():
    test = CPU
    #print(test.printData(test))
    test.pipeline[1] = '1'
    test.pipeline[2] = '2'
    test.pipeline[3] = '3'
    test.pipeline[4] = '4'
    test.pipeline[5] = '5'
    print(test.pipeline)
    test.cycle(test)
    print(test.pipeline)
    test.cycle(test)
    print(test.pipeline)

if __name__ == "__main__":
    main()