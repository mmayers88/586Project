
bin = []
file = open("sample_memory_image.txt", 'r')
read = file.readlines()
for i in read:
    bina = "{0:032b}".format(int(i,16))
    bin.append(bina)
print(read)
for i in bin:
    print(i)