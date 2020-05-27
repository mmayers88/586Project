
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
            Imm = ADDr[16:32]
            self.pipeline['ID']['IMM'] = Imm
            #print(ADDr)
            #print(RS, RT, Imm)
            return
        ADDr = data
        RS = ADDr[6:11]
        self.pipeline['ID']['RS'] = int(RS,2)
        RT = ADDr[11:16]
        self.pipeline['ID']['RT'] = int(RT,2)
        RD = ADDr[16:21]
        self.pipeline['ID']['RD']= int(RD,2)
        #print(ADDr)
        #print(RS, RT, RD)
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
        if self.pipeline['ID']['Type'] == 'R' or self.pipeline['ID']['OPCODE'] == 'STW':
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
        #if it is, stall
        #print(self.pipeline['ID'])
        return

    #execute Instruction
    def EX(self):
        if self.pipeline['EX']['data'] == 'x':
            return
        if self.pipeline['EX']['Type'] == 'H':
            return 'H'
        #use opcodes to do different things
        if self.pipeline['EX']['Type'] == 'R':
            #get values
            RS = self.Reg[self.pipeline['EX']['RS']]
            RT = self.Reg[self.pipeline['EX']['RT']]
            if RS !=0:
                if RS[0] == 1:
                    RS = int(RS, 2)
                    RS = -1 * RS
                else:
                    RS = int(RS, 2)
            if RT != 0:
                if RT[0] == 1:
                    RT = int(RT, 2)
                    RT = -1 * RT
                else:
                    RT = int(RT, 2)
            if self.pipeline['EX']['OPCODE'] == 'ADD':
                self.pipeline['EX']['Answer'] = self.ADD(RS,RT)
            if self.pipeline['EX']['OPCODE'] == 'SUB':
                self.pipeline['EX']['Answer'] = self.SUB(RS,RT)
            if self.pipeline['EX']['OPCODE'] == 'MUL':
                self.pipeline['EX']['Answer'] = self.MUL(RS,RT)
            if self.pipeline['EX']['OPCODE'] == 'AND':
                self.pipeline['EX']['Answer'] = self.AND(self.Reg[self.pipeline['EX']['RS']],self.Reg[self.pipeline['EX']['RT']])
            if self.pipeline['EX']['OPCODE'] == 'OR':
                self.pipeline['EX']['Answer'] = self.OR(self.Reg[self.pipeline['EX']['RS']],self.Reg[self.pipeline['EX']['RT']])
            if self.pipeline['EX']['OPCODE'] == 'XOR':
                self.pipeline['EX']['Answer'] = self.XOR(self.Reg[self.pipeline['EX']['RS']],self.Reg[self.pipeline['EX']['RT']])
            return
        else:
            RS = self.Reg[self.pipeline['EX']['RS']]
            IMM = self.pipeline['EX']['IMM']
            if RS != 0:
                if RS[0] == 1:
                    RS = int(RS, 2)
                    RS = -1 * RS
                else:
                    RS = int(RS, 2)
            if IMM[0] == 1:
                IMM = int(IMM, 2)
                IMM = -1 * IMM
            else:
                    IMM = int(IMM, 2)
            if self.pipeline['EX']['OPCODE'] == 'ADDI':
                self.pipeline['EX']['Answer'] = self.ADDI(RS,IMM)
            if self.pipeline['EX']['OPCODE'] == 'SUBI':
                self.pipeline['EX']['Answer'] = self.SUBI(RS,IMM)
            if self.pipeline['EX']['OPCODE'] == 'MULI':
                self.pipeline['EX']['Answer'] = self.MULI(RS,IMM)
            if self.pipeline['EX']['OPCODE'] == 'ANDI':
                self.pipeline['EX']['Answer'] = self.ANDI(self.Reg[self.pipeline['EX']['RS']],self.pipeline['EX']['IMM'])
            if self.pipeline['EX']['OPCODE'] == 'ORI':
                self.pipeline['EX']['Answer'] = self.ORI(self.Reg[self.pipeline['EX']['RS']],self.pipeline['EX']['IMM'])
            if self.pipeline['EX']['OPCODE'] == 'XORI':
                self.pipeline['EX']['Answer'] = self.XORI(self.Reg[self.pipeline['EX']['RS']],self.pipeline['EX']['IMM'])
            if self.pipeline['EX']['OPCODE'] == 'LDW':
                self.pipeline['EX']['Answer'] = self.LDW(self.Reg[self.pipeline['EX']['RS']],self.pipeline['EX']['IMM'])
            if self.pipeline['EX']['OPCODE'] == 'STW':
                self.pipeline['EX']['Answer'] = self.STW(self.Reg[self.pipeline['EX']['RS']],self.pipeline['EX']['IMM'])
            return
            '''
        if self.pipeline['EX']['OPCODE'] == 'BEQ' or self.pipeline['EX']['OPCODE'] == 'BZ' or self.pipeline['EX']['OPCODE'] == 'JR':
            if self.pipeline['EX']['OPCODE'] == 'BEQ':
                self.BEQ(self.pipeline['EX']['RS'],self.pipeline['EX']['IMM'])
            if self.pipeline['EX']['OPCODE'] == 'BZ':
                self.BZ(self.pipeline['EX']['RS'],self.pipeline['EX']['IMM'])
            if self.pipeline['EX']['OPCODE'] == 'JR':
                self.JR(self.pipeline['EX']['RS'],self.pipeline['EX']['IMM'])
            return
            '''
        return

    #memory
    #load or store from or to memory
    def MEM(self):
        if self.pipeline['MEM']['data'] == 'x' or self.pipeline['MEM']['Type'] == 'H':
            return
        if self.pipeline['MEM']['OPCODE'] != 'LDW' and self.pipeline['MEM']['OPCODE'] != 'STW':
            #only load and stores will do anything this step
            return
        #do load or store
        Address = int(self.pipeline['MEM']['Answer'],2)
        Address = Address >> 2
        print("Line: ", Address)
        if self.pipeline['MEM']['OPCODE'] == 'LDW':
            print("Do Load")
            bina = "{0:032b}".format(int(self.memory[Address],16))
            print("Load Data: ",bina)
            self.pipeline['MEM']['Answer'] = int(bina,2)
        else:
            print("Do Store")
            #the data below will need to be written back to memory
            print("Data Store: ", "{0:08X}".format(int(self.Reg[self.pipeline['MEM']['RT']], 2)))
        return

    #write back instruction
    #write back to register
    def WB(self):
        if self.pipeline['WB']['data'] == 'x':
            return
        if self.pipeline['WB']['OPCODE'] == 'STW' or self.pipeline['WB']['OPCODE'] == 'BZ' or self.pipeline['WB']['OPCODE'] == 'BEQ' or self.pipeline['WB']['OPCODE'] == 'JR':
            #these write nothing back
            return
        if self.pipeline['WB']['Type'] == 'R':
            self.Reg[self.pipeline['WB']['RD']] = '{0:032b}'.format(self.pipeline['WB']['Answer'])
        else:
            self.Reg[self.pipeline['WB']['RT']]= '{0:032b}'.format(self.pipeline['WB']['Answer'])

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
        #self.pipeline['EX']['Answer'] = self.ADD(RS,RT)
        answer = RS + RT
        return answer

    def ADDI(self,RS,IMM):
        answer = RS + IMM
        return answer
    def SUB(self, RS, RT):
        answer = RS - RT
        return answer

    def SUBI(self, RS, IMM):
        answer = RS - IMM
        return

    def MUL(self, RS, RT):
        answer = RS * RT
        return answer

    def MULI(self, RS, IMM):
        answer = RS * IMM
        return
        
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

    def LDW(self,RS, IMM):
        RS = int(RS, 2)
        if IMM[0] == 1:
            IMM = int(IMM, 2)
            IMM = -1 * IMM
        else:
            IMM = int(IMM, 2)
        Address = RS + IMM
        Answer = '{0:032b}'.format(Address)
        return Answer

    def STW(self,RS, IMM):
        RS = int(RS, 2)
        if IMM[0] == 1:
            IMM = int(IMM, 2)
            IMM = -1 * IMM
        else:
            IMM = int(IMM, 2)
        Address = RS + IMM
        Answer = '{0:032b}'.format(Address)
        return Answer
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
        #MEM
        self.MEM()
        #WB
        self.WB()
        #EX
        if self.EX() == 'H':
            return 'H'
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