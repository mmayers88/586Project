import pipeLine as pl 
import sys,os

try:
    fileName = sys.argv[1]
    print(fileName)
except:
    sys.exit(os.EX_IOERR) #can't find 'memory' so this returns IO error :p

test = pl.CPU(fileName)

print(test.printData())

for i in range(10):
    test.cycle()
    print(test.printData())