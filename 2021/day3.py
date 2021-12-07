import numpy as np

def getData():
    with open('dataDay3.txt','r') as file:
        data = file.read().split('\n')
        file.close()
    return data

def part1(data):
    gammaRate = ""
    gammaRateTot = [0 for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            gammaRateTot[j] += int(data[i][j])
            if (i == len(data)-1):
                gammaRateTot[j] = gammaRateTot[j]/len(data)
                if gammaRateTot[j] < 0.5:
                    gammaRate += '0'
                else:
                    gammaRate +='1'
    epsilonRate = ''
    for i in range(len(gammaRate)):
        if gammaRate[i] =='0':
            epsilonRate += '1'
        else:
            epsilonRate += '0'
    
    answer = int(gammaRate,2)*int(epsilonRate,2)
    return answer

def part2(data):
    oxy = data[:]
    co2 = data[:]
    for i in range(len(oxy[0])):
        bitCrit = 0
        for j in range(len(oxy)):
            bitCrit += int(oxy[j][i])
            if (j) == len(oxy)-1:
                mostCom = bitCrit/len(oxy)
                if mostCom < 0.5:
                    crit = '0'
                else:
                    crit='1'
        for j in range(len(oxy)-1,-1,-1):
            if oxy[j][i] != crit:
                 del oxy[j]
    
    for i in range(len(co2[0])):
        bitCrit = 0
        for j in range(len(co2)):
            bitCrit += int(co2[j][i])
            if (j) ==  len(co2)-1:
                mostCom = bitCrit/len(co2)
                if mostCom < 0.5:
                    crit = '0'
                else:
                    crit='1'
        for j in range(len(co2)-1,-1,-1):
            if co2[j][i] == crit:
                del co2[j]
        if len(co2) ==1:
            break
    print(oxy)
    print(co2)
    result = int(oxy[0],2)*int(co2[0],2)
    return result


def main():
    data = getData()
    answer = part1(data)
    print(answer)
    answer2 = part2(data)
    print(answer2)

main()