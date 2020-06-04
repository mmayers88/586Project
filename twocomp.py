def BintoInt(binNum):
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

def inttoBin(intNum):
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
    

def main():
    x = '11111011'
    print(BintoInt(x))
    x = '00000101'
    print(BintoInt(x))

    x = 0
    y = inttoBin(x)
    print(y)
    print(BintoInt(y))
if __name__ == "__main__":
    main()