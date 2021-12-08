def getData():
    with open('dataDay8.txt','r') as file:
        data = file.read().split('\n')
    data=[data[i].split(' | ') for i in range(len(data))]
    return data

def part1(data):
    numberOfDigits = 0
    for i in range(len(data)):
        fourDigit = data[i][1].split(' ')
        for j in range(len(fourDigit)):
            if len(fourDigit[j]) ==2 or len(fourDigit[j]) ==3 or len(fourDigit[j]) ==4 or len(fourDigit[j]) ==7:
                numberOfDigits += 1
    return numberOfDigits

def part2(data):
    outputNumbers = []
    for i in range(len(data)):
        fourDigit = data[i][1].split(' ')
        allNum = data[i][0].split(' ')
        allNumCheck = allNum[:]
        number = ''
        
        for j in range(len(allNum)):
            if len(allNum[j]) == 2:
                one = allNum[j]
                indexOne = j
            if len(allNum[j]) == 3:
                seven = allNum[j]
                indexSeven = j
            if len(allNum[j]) == 4:
                four = allNum[j]
                indexFour = j
            if len(allNum[j]) == 7:
                eight = allNum[j]
                indexEigth = j
        
        for l in range(len(allNum)):
            if len(allNum[l]) == 5 and stringCheck(allNum[l],one):
                three = allNum[l]
                indexThree = l
        for l in range(len(allNum)):
            if len(allNum[l]) ==6 and stringCheck(allNum[l],three) == 0 and stringCheck(allNum[l],one):
                zero = allNum[l]
                indexZero = l
        for l in range(len(allNum)):
            if len(allNum[l]) ==6 and stringCheck(allNum[l],one) == 0:
                six = allNum[l]
                indexSix = l
        for l in range(len(allNum)):
            if len(allNum[l]) ==6 and l != indexSix and l!= indexZero:
                nine = allNum[l]
                indexNine = l
        eightCopie = eight
        for l in range(len(six)):
            if six[l] in eightCopie:
                eightCopie = eightCopie.replace(six[l],'')
        
        for l in range(len(allNum)):
            if len(allNum[l]) ==5 and l!=indexThree and eightCopie in allNum[l]:
                two = allNum[l]
                indexTwo = l
        for l in range(len(allNum)):
            if len(allNum[l]) ==5 and l!=indexThree and l != indexTwo:
                five = allNum[l]
                indexFive = l
        print(i)   
        for j in range(len(fourDigit)):
            if sorted(fourDigit[j]) == sorted(one):
                number+='1'
            if sorted(fourDigit[j]) == sorted(two):
                number+='2'
            if sorted(fourDigit[j]) == sorted(three):
                number+='3'
            if sorted(fourDigit[j]) == sorted(four):
                number+='4'
            if sorted(fourDigit[j]) == sorted(five):
                number+='5'
            if sorted(fourDigit[j]) == sorted(six):
                number+='6'
            if sorted(fourDigit[j]) == sorted(seven):
                number+='7'
            if sorted(fourDigit[j]) == sorted(eight):
                number+='8'
            if sorted(fourDigit[j]) == sorted(nine):
                number+='9'
            if sorted(fourDigit[j]) == sorted(zero):
                number+='0'
        outputNumbers.append(int(number))
    result = sum(outputNumbers)
    return result

def stringCheck(string,substring):
    return all(string.count(i)>=substring.count(i) for i in substring)
    

def main():
    data = getData()
    answer1 = part1(data)
    print(answer1)

    answer2 = part2(data)
    print(answer2)

main()
