
class CPU:
    pipeline = {'IF':{'data': 'x', 'Type': 'x', 'OPCODE':'x', 'SOR1': 'x', 'SOR2': 'x', 'DEST': 'x', 'Answer': 'x',  'Stall': 'N'}, 
    'ID': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'SOR1': 'x', 'SOR2': 'x', 'DEST': 'x', 'Answer': 'x',  'Stall': 'N'},
    'EX': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'SOR1': 'x', 'SOR2': 'x', 'DEST': 'x', 'Answer': 'x',  'Stall': 'N'},
    'MEM': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'SOR1': 'x', 'SOR2': 'x', 'DEST': 'x', 'Answer': 'x',  'Stall': 'N'}, 
    'WB': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'SOR1': 'x', 'SOR2': 'x', 'DEST': 'x', 'Answer': 'x',  'Stall': 'N'}}
    PC = 0
    #registers 0-31 initialized to 0, Reg[0] will remain 0
    Reg = [0 for i in range(32)]
    destRegList = []
    def __init__(self, fileName):
        self.fileName = open(fileName, 'r')
        self.memory = self.fileName.readlines()
        #first IF
        self.IF()
        return      

    def printData(self):
        print(self.PC)
        print(self.Reg)
        for stage in self.pipeline:
            print(self.pipeline[stage])
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
        #print(self.pipeline['IF']['data'])
        self.pipeline['IF']['data'] = bina
        self.PC +=1
        return

    #instruction decode
    def ID(self):
        #first check Type
        #check opcode
        #with opcode information, format sources, destinations and immediates

        #ID must check if source register is a destination
        #if it is, stall
        return

    #execute Instruction
    def EX(self):
        if self.pipeline['EX']['data'] == 'x':
            return
        return

    #memory
    #load or store from or to memory
    def MEM(self):
        if self.pipeline['MEM']['data'] == 'x':
            return
        return

    #write back instruction
    #write back to register
    def WB(self):
        if self.pipeline['WB']['data'] == 'x':
            return
        if self.pipeline['WB']['Type'] == 'H':
            return 'H'
        return


    def iORrORn(self):
        #6 MSB are the opcode
        return

    def JR(self,address):
        jumpTo = address >> 5
        self.PC = jumpTo
        return

    #this will be the "main" function basically
    def cycle(self):
        #WB
        if self.WB() == 'H':
            return 'H'
        #MEM
        #EX
        #ID

        #increment pipeline
        self.pipeline['WB'] = self.pipeline['MEM']
        self.pipeline['MEM'] = self.pipeline['EX']
        if self.pipeline['ID']['Stall'] == 'Y':
            self.pipeline['EX'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'SOR1': 'x', 'SOR2': 'x', 'DEST': 'x', 'Answer': 'x',  'Stall': 'N'}
            return
        self.pipeline['EX'] = self.pipeline['ID']
        self.pipeline['ID'] = self.pipeline['IF']
        self.pipeline['IF'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'SOR1': 'x', 'SOR2': 'x', 'DEST': 'x', 'Answer': 'x',  'Stall': 'N'}
        #IF
        self.IF()
        return


def main():
    test = CPU("sample_memory_image.txt")


    print(test.printData())
    
    for i in range(10):
        test.cycle()
        print(test.printData())
    

if __name__ == "__main__":
    main()