
fileName = "sample_memory_image.txt"

memory = open(fileName, 'r')
PC = 0
lines = memory.readlines()
#print(lines)


while PC < len(lines):
    print(lines[PC])
    PC += 1