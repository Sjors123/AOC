

def getData():
    with open('dataDay4.txt','r') as file:
        data = file.read().split('\n')
        file.close()
    return data

def part1(data):
    bingoNumbers = data.pop(0).split(',')
    BingoCards = data[:]

    for i in range(len(bingoNumbers)):
        if len(bingoNumbers[i]) == 1:
            bingoNumbers[i] = '0'+ bingoNumbers[i]
    result = 0
    for i in range(len(BingoCards)-1,-1,-1):
        if '  ' in BingoCards[i]:
            BingoCards[i] = BingoCards[i].replace('  ',' 0')
        if BingoCards[i][:1] == ' ':
            BingoCards[i] = '0' + BingoCards[i][1:]
        if BingoCards[i] == '':
            del BingoCards[i]
        else:
            BingoCards[i] = BingoCards[i].split(' ')
    
    tweedeDeelData = data[300:]
    for i in range(len(bingoNumbers)):
        rowCount = 0
        puzzleCount = 0
        for j in range(len(BingoCards)):
            rowCount+=1
            bingoCount = 0
            for k in range(len(BingoCards[0])):
                if (BingoCards[j][k]) == (bingoNumbers[i]):
                    BingoCards[j][k] = 'Bingo'
                if BingoCards[j][k] == 'Bingo':
                    bingoCount +=1
                if bingoCount == 5:
                    sum = 0
                    for l in range(0,5):
                        for m in range(0,5):
                            if BingoCards[puzzleCount*5+l][m] != 'Bingo':
                                sum += int(BingoCards[puzzleCount*5+l][m])
                                print(puzzleCount*5+l)
                                print(m)
                                print(sum)
                    
                    result = int(bingoNumbers[i])*sum
                    return result
            if rowCount == 5:
                rowCount = 0
                puzzleCount +=1
        for j in range(len(BingoCards[0])):
            bingoCount = 0
            rowCount = 0
            puzzleCount = 0
            for k in range(len(BingoCards)):
                rowCount += 1
                if BingoCards[k][j] == 'Bingo':
                    bingoCount +=1
                if bingoCount ==5 and rowCount ==5:
                    sum = 0
                    for l in range(0,5):
                        for m in range(0,5):
                            if BingoCards[puzzleCount*5+l][m] != 'Bingo':
                                sum += int(BingoCards[puzzleCount*5+l][m])
                    result = int(bingoNumbers[i])*sum
                    return result
                if rowCount == 5:
                    rowCount = 0
                    puzzleCount += 1
                    bingoCount = 0

def part2(data):
    bingoNumbers = data.pop(0).split(',')
    BingoCards = data[:]

    for i in range(len(bingoNumbers)):
        if len(bingoNumbers[i]) == 1:
            bingoNumbers[i] = '0'+ bingoNumbers[i]

    for i in range(len(BingoCards)-1,-1,-1):
        if '  ' in BingoCards[i]:
            BingoCards[i] = BingoCards[i].replace('  ',' 0')
            data[i] = data[i].replace('  ',' 0')
        if BingoCards[i][:1] == ' ':
            BingoCards[i] = '0' + BingoCards[i][1:]
            data[i] = '0' + data[i][1:]
        if BingoCards[i] == '':
            del BingoCards[i]
            del data[i]
        else:
            BingoCards[i] = BingoCards[i].split(' ')
            data[i] = data[i].split(' ')

    
    
    for i in range(len(bingoNumbers)):
        rowCount = 0
        puzzleCount = 0
        for j in range(len(BingoCards)):
            rowCount+=1
            bingoCount = 0
            for k in range(len(BingoCards[0])):
                if (BingoCards[j][k]) == (bingoNumbers[i]):
                    BingoCards[j][k] = 'Bingo'
                if BingoCards[j][k] == 'Bingo':
                    bingoCount +=1
                if bingoCount == 5:
                    sum = 0
                    for l in range(0,5):
                        for m in range(0,5):
                            if(xCount == 25):
                                if(BingoCards[(puzzleCount)*5+l][m]!= 'Bingo'):
                                    sum+=int(BingoCards[(puzzleCount)*5+l][m])
                            else:
                                BingoCards[(puzzleCount)*5+l][m] = 'x'
                    if(xCount==25):
                        result = sum*int(bingoNumbers[i])
                        return result
                            
            if rowCount == 5:
                rowCount = 0
                puzzleCount +=1
        for j in range(len(BingoCards[0])):
            bingoCount = 0
            rowCount = 0
            puzzleCount = 0
            for k in range(len(BingoCards)):
                rowCount += 1
                if BingoCards[k][j] == 'Bingo':
                    bingoCount +=1
                if bingoCount ==5 and rowCount ==5:
                    sum = 0
                    for l in range(0,5):
                        for m in range(0,5):
                            if(xCount == 25):
                                if(BingoCards[(puzzleCount)*5+l][m]!= 'Bingo'):
                                    sum+=int(BingoCards[(puzzleCount)*5+l][m])
                            else:
                                BingoCards[(puzzleCount)*5+l][m] = 'x'
                    if(xCount==25):
                        result = sum*int(bingoNumbers[i])
                        return result
                if rowCount == 5:
                    rowCount = 0
                    puzzleCount += 1
                    bingoCount = 0
        xCount = 0 
        sum = 0
        for j in range(len(BingoCards)):
            for k in range(len(BingoCards[0])):
                if BingoCards[j][k] != 'x':
                    xCount +=1
                    if BingoCards[j][k] != 'Bingo':
                        sum += int(BingoCards[j][k])



        
def main():
    data = getData()
    result = part1(data)
    print(result)
    data2 = getData()
    result2 = part2(data2)
    print(result2)
main()