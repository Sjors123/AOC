import numpy as np

def getData():
    with open('dataDay2.txt','r') as file:
        data = file.read().split('\n')
        file.close()
    return data

def part1(data):
    hPos = 0
    depth = 0

    for i in range(len(data)):
        if 'up' in data[i]:
            depth -= int(data[i][-1])
        if 'down' in data[i]:
            depth += int(data[i][-1])
        if 'forward' in data[i]:
            hPos += int(data[i][-1])
    result = hPos*depth
    return result

def part2(data):
    aim = 0
    depth = 0
    hPos = 0
    for i in range(len(data)):
        if 'up' in data[i]:
            aim -= int(data[i][-1])
        if 'down' in data[i]:
            aim += int(data[i][-1])
        if 'forward' in data[i]:
            hPos += int(data[i][-1])
            depth += aim*int(data[i][-1])
    result = hPos*depth
    return result

def main():
    data = getData()
    answerPart1 = part1(data)
    print(answerPart1)
    answerPart2 = part2(data)
    print(answerPart2)

main()