
class CPU:
    pipeline = {1:'x', 2: 'x', 3: 'x', 4: 'x', 5: 'x'}
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
        self.pipeline[1] = bina
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
        self.pipeline[5] = self.pipeline[4]
        self.pipeline[4] = self.pipeline[3]
        self.pipeline[3] = self.pipeline[2]
        self.pipeline[2] = self.pipeline[1]
        self.pipeline[1] = 'x'
        return


def main():
    test = CPU("sample_memory_image.txt")
    #print(test.printData(test))
    test.pipeline[1] = '1'
    test.pipeline[2] = '2'
    test.pipeline[3] = '3'
    test.pipeline[4] = '4'
    test.pipeline[5] = '5'
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