# check ID to see if REG data has been forwarded
def checkFWD(self):
    if self.pipeline['ID']['Stall'] == 'Y':
        for x in self.tempRegList:
            if self.pipeline['ID']['RS'] == x:
                self.pipeline['ID']['Stall'] = 'F'
    
        if self.pipeline['ID']['Type'] == 'R' or self.pipeline['ID']['OPCODE'] == 'STW':
            for x in self.tempRegList:
                if self.pipeline['ID']['RT'] == x:
                    self.pipeline['ID']['Stall'] = 'F'
                    return
        

# change EX stage to grab correct forwarding data
if self.pipeline['EX']['Stall'] == 'F':
    for x in self.tempRegList:
        if self.pipeline['EX']['RS'] == x:
            RS = self.buffReg[self.pipeline['EX']['RS']]
            break
        else:
            RS = self.Reg[self.pipeline['EX']['RS']]

if self.pipeline['EX']['Stall'] == 'F':
    for x in self.tempRegList:
        if self.pipeline['EX']['RT'] == x:
            RT = self.buffReg[self.pipeline['EX']['RT']]
            break
        else:
            RT = self.Reg[self.pipeline['EX']['RT']]
