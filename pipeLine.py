
class CPU:
    pipeline = {'IF':{'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}, 
    'ID': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'},
    'EX': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'},
    'MEM': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}, 
    'WB': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}}
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
        print("PC: ",self.PC)
        print("Register Contents: ",self.Reg)
        print("Taken Registers: ",self.destRegList)
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
    def setSource(self,data,Type):
        if Type == 'I':
            ADDr = data
            RS = ADDr[6:11]
            self.pipeline['ID']['RS'] = int(RS,2)
            RT = ADDr[11:16]
            self.pipeline['ID']['RT'] = int(RT,2)
            Imm = ADDr[17:32]
            if ADDr[16] == 1:
                self.pipeline['ID']['IMM'] = -1 * int(Imm,2)
                return
            self.pipeline['ID']['IMM'] = int(Imm,2)
            print(ADDr)
            print(RS, RT, Imm)
            return
        ADDr = data
        RS = ADDr[6:11]
        self.pipeline['ID']['RS'] = int(RS,2)
        RT = ADDr[11:16]
        self.pipeline['ID']['RT'] = int(RT,2)
        RD = ADDr[16:21]
        self.pipeline['ID']['RD']= int(RD,2)
        print(ADDr)
        print(RS, RT, RD)
        return
    def decode(self,opInt):
        if opInt == 17:
            #halt
            self.pipeline['ID']['Type'] = 'H'
            self.pipeline['ID']['OPCODE'] = 'HALT'
            return
        if opInt < 6:
            #arithmatic
            if opInt == 0:
                self.pipeline['ID']['Type'] = 'R'
                self.pipeline['ID']['OPCODE'] = 'ADD'
                self.setSource(self.pipeline['ID']['data'],'R')
                return
            if opInt == 1:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'ADDI'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
            if opInt == 2:
                self.pipeline['ID']['Type'] = 'R'
                self.pipeline['ID']['OPCODE'] = 'SUB'
                self.setSource(self.pipeline['ID']['data'],'R')
                return
            if opInt == 3:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'SUBI'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
            if opInt == 4:
                self.pipeline['ID']['Type'] = 'R'
                self.pipeline['ID']['OPCODE'] = 'MUL'
                self.setSource(self.pipeline['ID']['data'],'R')
                return
            if opInt == 5:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'MULI'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
        if opInt >= 6 and opInt <= 11:
            #logical
            if opInt == 6:
                self.pipeline['ID']['Type'] = 'R'
                self.pipeline['ID']['OPCODE'] = 'OR'
                self.setSource(self.pipeline['ID']['data'],'R')
                return
            if opInt == 7:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'ORI'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
            if opInt == 8:
                self.pipeline['ID']['Type'] = 'R'
                self.pipeline['ID']['OPCODE'] = 'AND'
                self.setSource(self.pipeline['ID']['data'],'R')
                return
            if opInt == 9:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'ANDI'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
            if opInt == 10:
                self.pipeline['ID']['Type'] = 'R'
                self.pipeline['ID']['OPCODE'] = 'XOR'
                self.setSource(self.pipeline['ID']['data'],'R')
                return
            if opInt == 11:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'XORI'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
        if opInt >= 12 and opInt <= 13:
            #mem access
            if opInt == 12:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'LDW'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
            if opInt == 13:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'STW'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
        if opInt > 13:
            #flow control
            if opInt == 14:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'BZ'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
            if opInt == 15:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'BEQ'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
            if opInt == 16:
                self.pipeline['ID']['Type'] = 'I'
                self.pipeline['ID']['OPCODE'] = 'JR'
                self.setSource(self.pipeline['ID']['data'],'I')
                return
    #instruction decode
    def ID(self):
        if self.pipeline['ID']['data'] == 'x':
            return
        opInt = self.pipeline['ID']['data']
        opInt = opInt[0:6]
        self.decode(int(opInt,2))
        if self.pipeline['ID']['OPCODE'] == 'HALT':
            return

        #ID must check if source register is a destination
        if self.pipeline['ID']['OPCODE'] != 'STW':
            for x in self.destRegList:
                if self.pipeline['ID']['RS'] == x:
                    self.pipeline['ID']['Stall'] = 'Y'
                    #print(self.pipeline['ID'])
                    print("STALL")
                    return
        if self.pipeline['ID']['Type'] == 'R':
            for x in self.destRegList:
                if self.pipeline['ID']['RT'] == x:
                    self.pipeline['ID']['Stall'] = 'Y'
                    #print(self.pipeline['ID'])
                    print("STALL")
                    return
        self.pipeline['ID']['Stall'] = 'N'
        if self.pipeline['ID']['Type'] == 'R':
            self.destRegList.append(self.pipeline['ID']['RD'])
        if self.pipeline['ID']['OPCODE'][-1] == 'I' or self.pipeline['ID']['OPCODE'] == 'LDW':
            self.destRegList.append(self.pipeline['ID']['RT'])
        if self.pipeline['ID']['OPCODE'] == 'STW':
            self.destRegList.append(self.pipeline['ID']['RS'])
        #if it is, stall
        #print(self.pipeline['ID'])
        return

    #execute Instruction
    def EX(self):
        if self.pipeline['EX']['data'] == 'x':
            return
        if self.pipeline['WB']['Type'] == 'H':
            return 'H'
        #use opcodes to do different things
        return

    #memory
    #load or store from or to memory
    def MEM(self):
        if self.pipeline['MEM']['data'] == 'x' or self.pipeline['MEM']['Type'] == 'H':
            return
        if self.pipeline['MEM']['OPCODE'] != 'LDW' or self.pipeline['MEM']['OPCODE'] != 'STW':
            #only load and stores will do anything this step
            return
        #do load or store

        #remove from destination list
        if self.pipeline['MEM']['OPCODE'] == 'STW':
            self.destRegList.remove(self.pipeline['MEM']['RS'])
        return

    #write back instruction
    #write back to register
    def WB(self):
        if self.pipeline['WB']['data'] == 'x':
            return
        if self.pipeline['WB']['OPCODE'] == 'STW' or self.pipeline['WB']['OPCODE'] == 'BZ' or self.pipeline['WB']['OPCODE'] == 'BEQ' or self.pipeline['WB']['OPCODE'] == 'JR':
            #these write nothing back
            return

        #do write back to register step then clear the register list
        if self.pipeline['WB']['OPCODE'] == 'LDW':
            self.destRegList.remove(self.pipeline['WB']['RT'])
            return
        if self.pipeline['WB']['OPCODE'][-1] == 'I':
            self.destRegList.remove(self.pipeline['WB']['RT'])
        else:
            self.destRegList.remove(self.pipeline['WB']['RD'])
        return


    def flush(self):
        self.pipeline['IF'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
        self.pipeline['ID'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
        return


    #EX functions
    def ADD(self, RS, RT):
        #self.pipeline['EX']['Answer'] = self.ADD(self.pipeline['EX']['RS'],self.pipeline['EX']['RT'])
        answer = RS + RT
        return answer

    def ADDI(self):
        return
    def SUB(self):
        return
    def SUBI(self):
        return
    def MUL(self):
        return
    def MULI(self):
        return
    def OR(self):
        return
    def ORI(self):
        return
    def AND(self):
        return
    def ANDI(self):
        return
    def XOR(self):
        return
    def XORI(self):
        return
    def LDW(self):
        return
    def STW(self):
        return
    def BZ(self):
        return
    def BEQ(self):
        return   
    def JR(self,address):
        jumpTo = address >> 2
        self.PC = jumpTo
        self.flush
        return

    #this will be the "main" function basically
    def cycle(self):
        #WB
        self.WB()
        #MEM
        #EX
        #ID
        self.ID()
        #increment pipeline
        self.pipeline['WB'] = self.pipeline['MEM']
        self.pipeline['MEM'] = self.pipeline['EX']
        if self.pipeline['ID']['Stall'] == 'Y':
            self.pipeline['EX'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
            return
        self.pipeline['EX'] = self.pipeline['ID']
        self.pipeline['ID'] = self.pipeline['IF']
        self.pipeline['IF'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
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