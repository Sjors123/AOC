
def getData():
    with open('dataDay6.txt','r') as file:
        data = file.read().split('\n')
        file.close()
    return data

def part1(initData):
    data = initData[0].split(',')
    for i in range(0,80):
        for j in range(len(data)):
            if int(data[j]) == 0:
                data[j] = 7
                data.append(8)
            data[j] = int(data[j]) -1
    return len(data)

def part2(initData):
    data = initData[0].split(',')
    numbers0 = [0,0]
    numbers1 = [0,0]
    numbers2 = [0,0]
    numbers3 = [0,0]
    numbers4 = [0,0]
    numbers5 = [0,0]
    numbers6 = [0,0]
    numbers7 = [0,0]
    numbers8 = [0,0]

    for i in range(len(data)):
        if data[i] == '0':
            numbers0[0] += 1
        if data[i] == '1':
            numbers1[0] += 1
        if data[i] == '2':
            numbers2[0] += 1
        if data[i][0] == '3':
            numbers3[0] += 1
        if data[i][0] == '4':
            numbers4[0] += 1
        if data[i][0] == '5':
            numbers5[0] += 1
        if data[i] == '6':
            numbers6[0] += 1

    for i in range(0,256):
        numbers8[1] = numbers0[0]
        numbers7[1] = numbers8[0]
        numbers6[1] = numbers7[0] + numbers0[0]
        numbers5[1] = numbers6[0]
        numbers4[1] = numbers5[0]
        numbers3[1] = numbers4[0]
        numbers2[1] = numbers3[0]
        numbers1[1] = numbers2[0]
        numbers0[1] = numbers1[0]

        numbers0[0] = numbers0[1]
        numbers1[0] = numbers1[1]
        numbers2[0] = numbers2[1]
        numbers3[0] = numbers3[1]
        numbers4[0] = numbers4[1]
        numbers5[0] = numbers5[1]
        numbers6[0] = numbers6[1]
        numbers7[0] = numbers7[1]
        numbers8[0] = numbers8[1]
    results  = numbers0[0]+numbers1[0]+numbers2[0]+numbers3[0]+numbers4[0]+numbers5[0]+numbers6[0]+numbers7[0]+numbers8[0]
    return results

def main():
    data = getData()
    # answer1 = part1(data)
    # print(answer1)

    answer2 =part2(data)
    print(answer2)

main()