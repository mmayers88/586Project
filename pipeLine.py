
class CPU:
    pipeline = {'IF':'x', 'ID': 'x', 'EX': 'x', 'MEM': 'x', 'WB': 'x'}
    PC = 0
    def __init__(self, fileName):
        self.fileName = open(fileName, 'r')
        self.memory = self.fileName.readlines()
        return      

    def printData(self):
        print(self.pipeline)
        print(self.PC)
        #print(self.memory)
        return
    
    def showMEM(self):
        for line in self.memory:
            print(line)

    #instruction fetch
    def IF(self):
        #integer
        inte = int(self.memory[self.PC],16)
        #binary
        bina = "{0:032b}".format(int(self.memory[self.PC],16))
        #hexadecimal
        hexa = hex(inte)
        #print(hexa)
        #string
        #print(self.memory[self.PC])
        #saving binary to pipeline
        self.pipeline['IF'] = bina
        self.PC +=1
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
        self.IF()
        #ID
        #EX
        #MEM
        #WB

        #increment pipeline
        self.pipeline['WB'] = self.pipeline['MEM']
        self.pipeline['MEM'] = self.pipeline['EX']
        self.pipeline['EX'] = self.pipeline['ID']
        self.pipeline['ID'] = self.pipeline['IF']
        self.pipeline['IF'] = 'x'
        return


def main():
    test = CPU("sample_memory_image.txt")
    #print(test.printData(test))
    test.pipeline['IF'] = {'OPCODE':'i', 'SOR1': 1, 'SOR2': 2, 'DEST': 3, 'Stall': 'N'}
    test.pipeline['ID'] = '2'
    test.pipeline['EX'] = '3'
    test.pipeline['MEM'] = '4'
    test.pipeline['WB'] = '5'
    print(test.pipeline)
    print(test.PC)
    test.cycle()
    print(test.pipeline)
    print(test.PC)
    test.cycle()
    print(test.pipeline)
    print(test.PC)
    test.cycle()
    print(test.pipeline)
    print(test.PC)
    test.cycle()
    print(test.pipeline)
    print(test.PC)
    #print(test.showMEM())

if __name__ == "__main__":
    main()