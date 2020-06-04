import pipeLine as pl 

fileName = 'final_proj_trace.txt'


'''
First Processor has no forwarding
'''
processor = pl.CPU(fileName,'N')

#processor.printData()

#waiting for halt

while processor.cycle() != 'H':
    #processor.printData()
    continue


print("***********************************************\n\nProcessor 1\nNo Forwarding: \n")
print("***********************************************\nRegisters: \n")
processor.printReg()
print("***********************************************\nFinal Pipeline State: \n")
processor.printData()
intCount = processor.AriCount + processor.LogCount + processor.MemCount + processor.ConCount
print("***********************************************\nCounts: \n")
print("Instruction Count: ", intCount)
print("Arithmetic Instructions: ", processor.AriCount)
print("Logical Instructions: ",processor.LogCount)
print("Memory Access Instructions: ",processor.MemCount)
print("Control Flow Instructions: ",processor.ConCount)
print("Stalls: ",processor.stalls)

print("\nMemChanged: ")
processor.printMEMchange()

'''
Processor 2 Code has forwarding
'''

processor2 = pl.CPU(fileName,'Y')

#waiting for halt

while processor2.cycle() != 'H':
    #processor2.printData()
    continue

print("\n\n***********************************************\n\nProcessor 2\nForwarding Enabled: \n")
print("***********************************************\nRegisters: \n")
processor2.printReg()
print("***********************************************\nFinal Pipeline State: \n")
processor2.printData()
intCount = processor2.AriCount + processor2.LogCount + processor2.MemCount + processor2.ConCount
print("***********************************************\nCounts: \n")
print("Instruction Count: ", intCount)
print("Arithmetic Instructions: ", processor2.AriCount)
print("Logical Instructions: ",processor2.LogCount)
print("Memory Access Instructions: ",processor2.MemCount)
print("Control Flow Instructions: ",processor2.ConCount)
print("Stalls: ",processor2.stalls)

print("\nMemChanged: ")
processor2.printMEMchange()

