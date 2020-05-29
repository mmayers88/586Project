import pipeLine as pl 
import sys, os

try:
    fileName = sys.argv[1]
    print(fileName)
except:
    sys.exit(os.EX_IOERR) #can't find 'memory' so this returns IO error :p
try:
    forwarding = sys.argv[2]
except:
    forwarding = 'N'

if forwarding != 'Y' or forwarding != 'y':
    forwarding = 'N'
else:
    forwarding = 'Y'


processor = pl.CPU(fileName,forwarding)

print(processor.printData())

#finite test
'''
for i in range(20):
    processor.cycle()
    print(processor.printData())
'''


#waiting for halt

while processor.cycle() != 'H':
    print(processor.printData())
    continue
print(processor.printData())
intCount = processor.AriCount + processor.LogCount + processor.MemCount + processor.ConCount
print("Instruction Count: ", intCount)
print("Arithmetic Instructions: ", processor.AriCount)
print("Logical Instructions: ",processor.LogCount)
print("Memory Access Instructions: ",processor.MemCount)
print("Control Flow Instructions: ",processor.ConCount)
print("Stalls: ",processor.stalls)
