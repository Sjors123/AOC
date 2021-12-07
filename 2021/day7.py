
def getData():
    with open('dataDay7.txt','r') as file:
        data = file.read().split(',')
    data=[int(i) for i in data]
    return data

def part1(data):
    lowestSum = max(data)**2
    for i in range(0,max(data)):
        sum = 0
        for j in range(len(data)):
            sum += abs(data[j]-i)
        if sum < lowestSum:
            lowestSum = sum
    return lowestSum

def part2(data):
    maxData = max(data)**2
    lowestSum = maxData*(maxData+1)/2
    for i in range(0,max(data)):
        sum = 0
        for j in range(len(data)):
            diff= abs(data[j]-i)
            sum += diff*(diff+1)/2
        if sum < lowestSum:
            lowestSum = sum
    return lowestSum

def main():
    data = getData()
    answer1 = part1(data)
    print(answer1)
    answer2 = part2(data)
    print(answer2)

main()