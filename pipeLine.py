
class CPU:
    pipeline = {'IF':{'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}, 
    'ID': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'},
    'EX': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'},
    'MEM': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}, 
    'WB': {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}}
    PC = 0
    #registers 0-31 initialized to 0, Reg[0] will remain 0
    Reg = [0 for i in range(32)]
    buffReg = [0 for i in range(32)]
    destRegList = []
    tempRegList = []
    storeList = []
    MemCount = 0
    AriCount = 0
    LogCount = 0
    ConCount = 0
    stalls = 0
    cycleC = 0
    nop1 = 0
    nop2 = 0
    instructionList = []
    def __init__(self, fileName, forwarding = 'N'):
        self.FWD = forwarding
        self.fileWord = fileName
        self.fileName = open(fileName, 'r')
        self.memory = self.fileName.readlines()
        self.fileName2 = open("out.txt", 'w')
        #first IF
        #self.IF()
        return      
    def printReg(self):
        for x in range(32):
            try:
                print( x, self.Reg[x], int(self.Reg[x],2))
            except:
                print(x, self.Reg[x], self.Reg[x])
    def printbuffReg(self):
        for x in range(32):
            try:
                print( x, self.buffReg[x], int(self.buffReg[x],2))
            except:
                print(x, self.buffReg[x], self.buffReg[x])

    def printMEMchange(self):
        for x in self.storeList:
            print("\t",x[0],':',x[1],'=',int(x[1],16))

    def printData(self):
        printPC = self.PC << 2
        print("PC: ",printPC)
        #print("Register Contents: ")
        #self.printReg()
        #print("Registers buff: ", self.tempRegList)
        #print("Taken Registers: ",self.destRegList)
        for stage in self.pipeline:
            print(self.pipeline[stage])
        #print("Cycle: ",self.cycleC)
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
        if self.pipeline['IF']['data'] == '00000000000000000000000000000000':
            self.pipeline['IF'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
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
        for x in self.destRegList:
            if self.pipeline['ID']['RS'] == x:
                self.pipeline['ID']['Stall'] = 'Y'
                self.stalls = self.stalls + 1
                print("STALL")
                return
        if self.pipeline['ID']['Type'] == 'R' or self.pipeline['ID']['OPCODE'] == 'STW':
            for x in self.destRegList:
                if self.pipeline['ID']['RT'] == x:
                    self.pipeline['ID']['Stall'] = 'Y'
                    self.stalls = self.stalls + 1
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
        self.instructionList.append(self.pipeline['EX'])
        if self.pipeline['EX']['Type'] == 'H':
            return
        #use opcodes to do different things
        if self.pipeline['EX']['OPCODE'] == 'BEQ' or self.pipeline['EX']['OPCODE'] == 'BZ' or self.pipeline['EX']['OPCODE'] == 'JR':

            if self.pipeline['EX']['Stall'] == 'F':
                for x in self.tempRegList:
                    if self.pipeline['EX']['RS'] == x:
                        RS = self.buffReg[self.pipeline['EX']['RS']]
                        break
                    else:
                        RS = self.Reg[self.pipeline['EX']['RS']]
                try:
                    for x in self.tempRegList:
                        if self.pipeline['EX']['RS'] == x:
                            RS = self.buffReg[self.pipeline['EX']['RS']]
                            break
                        else:
                            RS = self.Reg[self.pipeline['EX']['RS']]
                except:
                    print("continue stall")
            else:
                RS = self.Reg[self.pipeline['EX']['RS']]

            if self.pipeline['EX']['Stall'] == 'F':
                try:
                    for x in self.tempRegList:
                        if self.pipeline['EX']['RT'] == x:
                            RT = self.buffReg[self.pipeline['EX']['RT']]
                            break
                        else:
                            RT = self.Reg[self.pipeline['EX']['RT']]
                except:
                    print("continue stall")
            else:
                RT = self.Reg[self.pipeline['EX']['RT']]

            IMM = self.pipeline['EX']['IMM']
            
            self.ConCount =  self.ConCount + 1 
            if self.pipeline['EX']['OPCODE'] == 'BEQ':
                self.BEQ(RS,RT,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'BZ':
                self.BZ(RS,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'JR':
                self.JR(RS)
               #print(self.PC)
                return

        if self.pipeline['EX']['Type'] == 'R':
            #get values
            if self.pipeline['EX']['Stall'] == 'F':
                try:
                    for x in self.tempRegList:
                        if self.pipeline['EX']['RS'] == x:
                            RS = self.buffReg[self.pipeline['EX']['RS']]
                            break
                        else:
                            RS = self.Reg[self.pipeline['EX']['RS']]
                except:
                    print("continue stall")
            else:
                RS = self.Reg[self.pipeline['EX']['RS']]

            if self.pipeline['EX']['Stall'] == 'F':
                try:
                    for x in self.tempRegList:
                        if self.pipeline['EX']['RT'] == x:
                            RT = self.buffReg[self.pipeline['EX']['RT']]
                            break
                        else:
                            RT = self.Reg[self.pipeline['EX']['RT']]
                except:
                    print("continue stall")
            else:
                RT = self.Reg[self.pipeline['EX']['RT']]

            
            if self.pipeline['EX']['OPCODE'] == 'ADD':
                self.AriCount =  self.AriCount + 1
                self.pipeline['EX']['Answer'] = self.ADD(RS,RT)
                return
            if self.pipeline['EX']['OPCODE'] == 'SUB':
                self.AriCount =  self.AriCount + 1
                self.pipeline['EX']['Answer'] = self.SUB(RS,RT)
                return
            if self.pipeline['EX']['OPCODE'] == 'MUL':
                self.AriCount =  self.AriCount + 1
                self.pipeline['EX']['Answer'] = self.MUL(RS,RT)
                return
            if self.pipeline['EX']['OPCODE'] == 'AND':
                self.LogCount =  self.LogCount + 1
                self.pipeline['EX']['Answer'] = self.AND(RS,RT)
                return
            if self.pipeline['EX']['OPCODE'] == 'OR':
                self.LogCount =  self.LogCount + 1
                self.pipeline['EX']['Answer'] = self.OR(RS,RT)
                return
            if self.pipeline['EX']['OPCODE'] == 'XOR':
                self.LogCount =  self.LogCount + 1
                self.pipeline['EX']['Answer'] = self.XOR(RS,RT)
                return
        else:
            if self.pipeline['EX']['Stall'] == 'F':
                try:
                    for x in self.tempRegList:
                        if self.pipeline['EX']['RS'] == x:
                            RS = self.buffReg[self.pipeline['EX']['RS']]
                            break
                        else:
                            RS = self.Reg[self.pipeline['EX']['RS']]
                except:
                    print("continue stall")
            else:
                RS = self.Reg[self.pipeline['EX']['RS']]
            IMM = self.pipeline['EX']['IMM']
            
            if self.pipeline['EX']['OPCODE'] == 'ADDI':
                self.AriCount =  self.AriCount + 1
                self.pipeline['EX']['Answer'] = self.ADDI(RS,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'SUBI':
                self.AriCount =  self.AriCount + 1
                self.pipeline['EX']['Answer'] = self.SUBI(RS,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'MULI':
                self.AriCount =  self.AriCount + 1
                self.pipeline['EX']['Answer'] = self.MULI(RS,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'ANDI':
                self.LogCount =  self.LogCount + 1
                self.pipeline['EX']['Answer'] = self.ANDI(RS,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'ORI':
                self.LogCount =  self.LogCount + 1
                self.pipeline['EX']['Answer'] = self.ORI(RS,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'XORI':
                self.LogCount =  self.LogCount + 1
                self.pipeline['EX']['Answer'] = self.XORI(RS,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'LDW':
                self.MemCount =  self.MemCount + 1 
                self.pipeline['EX']['Answer'] = self.LDW(RS,IMM)
                return
            if self.pipeline['EX']['OPCODE'] == 'STW':
                self.MemCount =  self.MemCount + 1 
                self.pipeline['EX']['Answer'] = self.STW(RS,IMM)
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
        #print ("Address", Address)
        Address = Address >> 2
       #print("Line: ", Address)
        if self.pipeline['MEM']['OPCODE'] == 'LDW':
           #print("Do Load")
           #print(self.pipeline['MEM'])
            bina = "{0:032b}".format(int(self.memory[Address],16))
           #print("Load Data: ",bina)
            self.pipeline['MEM']['Answer'] = int(bina,2)
        else:
           #print("Do Store")
            #the data below will need to be written back to memory
           #print("Data Store: ", "{0:08X}".format(int(self.Reg[self.pipeline['MEM']['RT']], 2)))
            self.memory[Address] = "{0:08X}".format(int(self.Reg[self.pipeline['MEM']['RT']], 2)) + '\n'
            storeBack = (Address << 2,"{0:08X}".format(int(self.Reg[self.pipeline['MEM']['RT']], 2)))
            self.storeList.append(storeBack)
        return

    #write back instruction
    #write back to register
    def WB(self):
        if self.pipeline['WB']['data'] == 'x':
            if self.pipeline['WB']['OPCODE'] == 'NOP1':
                self.nop1 = self.nop1 +1
            if self.pipeline['WB']['OPCODE'] == 'NOP2':
                self.nop1 = self.nop1 - 1
                self.nop2 = self.nop2 +1 
            return
        if self.pipeline['WB']['Type'] == 'H':
            return 'H'
        if self.pipeline['WB']['OPCODE'] == 'STW' or self.pipeline['WB']['OPCODE'] == 'BZ' or self.pipeline['WB']['OPCODE'] == 'BEQ' or self.pipeline['WB']['OPCODE'] == 'JR':
            #these write nothing back
            return
        if self.pipeline['WB']['Type'] == 'R':
            Answer = self.inttoBin(self.pipeline['WB']['Answer'])
            self.Reg[self.pipeline['WB']['RD']] = Answer
        else:
            Answer = self.inttoBin(self.pipeline['WB']['Answer'])
            self.Reg[self.pipeline['WB']['RT']]= Answer

        #do write back to register step then clear the register list
        if self.pipeline['WB']['OPCODE'] == 'LDW':
            self.destRegList.remove(self.pipeline['WB']['RT'])
            if self.FWD == 'Y':
               self.tempRegList.remove(self.pipeline['WB']['RT'])
            return
        if self.pipeline['WB']['OPCODE'][-1] == 'I':
            self.destRegList.remove(self.pipeline['WB']['RT'])
            if self.FWD == 'Y':
                self.tempRegList.remove(self.pipeline['WB']['RT'])
        else:
            self.destRegList.remove(self.pipeline['WB']['RD'])
            if self.FWD == 'Y':
                self.tempRegList.remove(self.pipeline['WB']['RD'])
        return


    def flush(self):
        self.pipeline['IF'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
        self.pipeline['ID'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
        return


    #EX functions
    def ADD(self, RS, RT):
        if RS != 0 :
            RS = self.BintoInt(RS)
        if RT != 0:
            RT = self.BintoInt(RT)
        answer = RS + RT
        return answer

    def ADDI(self,RS,IMM):
        if RS != 0:
            RS = self.BintoInt(RS)
        IMM = self.BintoInt(IMM)
       #print(RS)
       #print(IMM)
        answer = RS + IMM
       #print("Answer: ", answer)
        return answer

    def SUB(self, RS, RT):
        if RS != 0 :
            RS = self.BintoInt(RS)
        if RT != 0:
            RT = self.BintoInt(RT)
       #print(RS)
       #print(RT)
        answer = RS - RT
        return answer

    def SUBI(self, RS, IMM):
        if RS != 0:
            RS = self.BintoInt(RS)
        IMM = self.BintoInt(IMM)
       #print(RS)
       #print(IMM)
        answer = RS - IMM
        return answer

    def MUL(self, RS, RT):
        if RS != 0 :
            RS = self.BintoInt(RS)
        if RT != 0:
            RT = self.BintoInt(RT)
        answer = RS * RT
        return answer

    def MULI(self, RS, IMM):
        if RS != 0:
            RS = self.BintoInt(RS)
        IMM = self.BintoInt(IMM)
        answer = RS * IMM
        return answer

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
       #print(RS)
        if RS != 0:
            RS = self.BintoInt(RS)
        IMM = self.BintoInt(IMM)
       #print(RS)
       #print(IMM)
        Address = RS + IMM
        '''
        if Address < 0:
                Answer = '{0:015b}'.format(Address)
                Answer = '1' + Answer[1:]
        else:
            Answer = '{0:016b}'.format(Address)
        if len(Answer) > 16:
            cut = len(Answer)-16
            Answer = Answer[cut:]
        '''
        Answer = self.inttoBin(Address)
        return Answer

    def STW(self,RS, IMM):
       #print(RS)
        if RS != 0:
            RS = self.BintoInt(RS)
        IMM = self.BintoInt(IMM)
       #print(RS)
       #print(IMM)
        Address = RS + IMM
        '''
        if Address < 0:
                Answer = '{0:015b}'.format(Address)
                Answer = '1' + Answer[1:]
        else:
            Answer = '{0:016b}'.format(Address)
        if len(Answer) > 16:
            cut = len(Answer)-16
            Answer = Answer[cut:]
        '''
        Answer = self.inttoBin(Address)
        return Answer

    def BZ(self, RS, IMM):
        if RS !=0:
            RS = self.BintoInt(RS)
        if IMM !=0:
            IMM = self.BintoInt(IMM)
        if RS == 0:
            #print ("Address", Address)
            #print("PC", self.PC)
           #print(IMM)
            self.PC = self.PC - 3 + IMM
            #print ("PC from IMM", self.PC)
            #Address = "{0:032b}".format(int(Address, 16))
            #self.PC = (Address -1) << 2
            self.flush()
        return

    def BEQ(self, RS, RT, IMM):
        if RS !=0:
            RS = int(RS, 2)
        if RT !=0:
            RT = int(RT, 2)
        if IMM !=0:
            IMM = self.BintoInt(IMM)
        if RS == RT:
            self.PC = self.PC - 3 + IMM
            #Address = "{0:032b}".format(int(Address,16))
            #self.PC = (Address - 1) << 2
            self.flush()
        return

    def JR(self,RS):
        if RS !=0:
            RS = self.BintoInt(RS)
        jumpTo = RS >> 2
        #jumpTo = RS
       #print("JumpTo: ",jumpTo)
        self.PC = jumpTo
       #print(self.PC)
        self.flush()
        return
    
    def checkFWD(self):
        a = 0
        b = 0
        c = 0
        d = 0
        if self.pipeline['ID']['Stall'] == 'Y':
            for x in self.tempRegList:
                if self.pipeline['ID']['RS'] == x:
                    a = 1
                    break
            for x in self.destRegList:
                if self.pipeline['ID']['RS'] == x:
                    b = 1
                    break
            if a ^ b != 0:
                return
            else:
                e = 1
            if self.pipeline['ID']['Type'] == 'R' or self.pipeline['ID']['OPCODE'] == 'STW':
                for x in self.tempRegList:
                    if self.pipeline['ID']['RT'] == x:
                        c = 1
                        break
                for x in self.destRegList:
                    if self.pipeline['ID']['RT'] == x:
                        d = 1
                if c ^ d != 0:
                    return
                else:
                    f = 1                      
            else:
                f = 1
            if e & f == 1:
                self.pipeline['ID']['Stall'] = 'F'
                self.stalls= self.stalls -1 
                if self.pipeline['ID']['Type'] == 'R':
                    self.destRegList.append(self.pipeline['ID']['RD'])
                if self.pipeline['ID']['OPCODE'][-1] == 'I' or self.pipeline['ID']['OPCODE'] == 'LDW':
                    self.destRegList.append(self.pipeline['ID']['RT'])
        
    def remFWD(self):
        if self.pipeline['EX']['Stall'] == 'F':
            for x in self.tempRegList:
                if self.pipeline['EX']['RS'] == x:
                    self.pipeline['EX']['Stall'] = 'F'
                    return
            if self.pipeline['EX']['Type'] == 'R' or self.pipeline['EX']['OPCODE'] == 'STW':
                for x in self.tempRegList:
                    if self.pipeline['EX']['RT'] == x:
                        self.pipeline['EX']['Stall'] = 'F'
                        return
            self.pipeline['EX']['Stall'] = 'N'

    def forwarding(self):
        if self.pipeline['EX']['data'] == 'x' or self.pipeline['EX']['Type'] == 'H':
            return
        if self.pipeline['EX']['OPCODE'] == 'LDW' or self.pipeline['EX']['OPCODE'] == 'STW' or self.pipeline['EX']['OPCODE'] == 'BZ' or self.pipeline['EX']['OPCODE'] == 'BEQ' or self.pipeline['EX']['OPCODE'] == 'JR':
            ##only opcodes that return data matter
            return
        if self.pipeline['EX']['Type'] == 'R':
            Answer = self.inttoBin(self.pipeline['EX']['Answer'])
            self.buffReg[self.pipeline['EX']['RD']] = Answer
        else:
            Answer = self.inttoBin(self.pipeline['EX']['Answer'])
            self.buffReg[self.pipeline['EX']['RT']]= Answer

        
        if self.pipeline['EX']['OPCODE'][-1] == 'I':
            self.tempRegList.append(self.pipeline['EX']['RT'])
        else:
            self.tempRegList.append(self.pipeline['EX']['RD'])
        return

    def forMEM(self):
        if self.pipeline['MEM']['data'] == 'x' or self.pipeline['MEM']['Type'] == 'H':
            return
        if self.pipeline['MEM']['OPCODE'] == 'LDW':
            Answer = self.inttoBin(self.pipeline['MEM']['Answer'])
            self.buffReg[self.pipeline['MEM']['RT']]= Answer
            self.tempRegList.append(self.pipeline['MEM']['RT'])
            return
        return

    def BintoInt(self,binNum):
        if binNum[0] == '1':
            newNum = ''
            for x in range(len(binNum)):
                if binNum[x] == '0':
                    newNum = newNum + '1'
                else:
                    newNum = newNum + '0'
            binNum = int(newNum,2)
            binNum = binNum + 1
            binNum = binNum * -1
        else:
            binNum = int(binNum,2)
        return binNum

    def inttoBin(self,intNum):
        if intNum < 0:
            intNum = '{0:032b}'.format(intNum)
            intNum =  intNum[1:]
            newNum = ''
            for x in range(len(intNum)):
                if intNum[x] == '0':
                    newNum = newNum + '1'
                else:
                    newNum = newNum + '0'         
            intNum = int(newNum,2)
            intNum = intNum + 1
            Answer = '{0:031b}'.format(intNum)
            Answer = '1'+Answer
        else:
            Answer = '{0:032b}'.format(intNum)
        return Answer
    #this will be the "main" function basically
    def cycle(self):
        self.cycleC=self.cycleC +1
        #MEM
        self.MEM()
            
        #WB
        if self.WB() == 'H':
            self.fileName2.writelines(self.memory)
            self.fileName2.close()
            self.ConCount = self.ConCount + 1
            self.PC=self.PC - 4
            return 'H'
        
        #EX
        if self.FWD == 'Y':
            self.remFWD()
        self.EX()
        if self.FWD == 'Y':
            self.forwarding()
            self.forMEM()
        #ID
        self.ID()
        self.checkFWD()
        #increment pipeline
        self.pipeline['WB'] = self.pipeline['MEM']
        self.pipeline['MEM'] = self.pipeline['EX']
        if self.pipeline['ID']['Stall'] != 'N' and self.pipeline['ID']['Stall'] != 'F':
            if self.pipeline['MEM']['OPCODE'] == 'NOP1':
                self.pipeline['EX'] = {'data': 'x', 'Type': 'x', 'OPCODE':'NOP2', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
            else:
                self.pipeline['EX'] = {'data': 'x', 'Type': 'x', 'OPCODE':'NOP1', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
            return
        self.pipeline['EX'] = self.pipeline['ID']
        self.pipeline['ID'] = self.pipeline['IF']
        self.pipeline['IF'] = {'data': 'x', 'Type': 'x', 'OPCODE':'x', 'RS': 'x', 'RT': 'x', 'RD': 'x', 'IMM':'x', 'Answer': 'x',  'Stall': 'N'}
        #IF
        self.IF()
        self.PC +=1
        return


def main():
    test = CPU("sample_memory_image.txt")


   #print(test.printData())
    
    for i in range(1000):
        test.cycle()
        test.printData()
    

if __name__ == "__main__":
    main()