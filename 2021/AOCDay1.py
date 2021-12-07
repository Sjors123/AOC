import numpy as np

def part1(data):
    depthCount = 0
    for i in range(len(data)-1):
        if(data[i+1]-data[i] > 0):
            depthCount +=1
    return depthCount

def part2(data):
    depthCount = 0
    for i in range(len(data)-3):
        if ( np.sum(data[i+1:i+4])> np.sum(data[i:i+3])):
            depthCount +=1
    return depthCount


def main():
    data = np.loadtxt('dataDay1.txt')
    answerPart1 = part1(data)
    print(answerPart1)
    answerPart2 = part2(data)
    print(answerPart2)

main()