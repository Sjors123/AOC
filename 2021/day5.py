
def getData():
    with open('dataDay5.txt','r') as file:
        data = file.read().split('\n')
        file.close()
    return data

def part1(data):
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for i in range(0,1000):
        for j in range(0,1000):
            grid[i][j] = "{},{}".format(i, j)
    intersect=0
    for i in range(len(data)):
        line = makeLine(data[i])
        if len(line)>0:
            for i in range(len(line)):
                coordinate = line[i].split(',')
                if grid[int(coordinate[0])][int(coordinate[1])] =='x':
                    intersect+=1
                    grid[int(coordinate[0])][int(coordinate[1])] ='L'
                if grid[int(coordinate[0])][int(coordinate[1])] !='x' and grid[int(coordinate[0])][int(coordinate[1])] !='L':
                    grid[int(coordinate[0])][int(coordinate[1])] ='x'
                
    return intersect

def makeLine(coordinates):
    
    splittedCoordinates = coordinates.split('->')
    coordinate1 = splittedCoordinates[0].replace(' ','').split(',')
    coordinate2 = splittedCoordinates[1].replace(' ','').split(',')
    line = []
    if coordinate1[0] != coordinate2[0] and coordinate1[1] != coordinate2[1]:
            return line
    if coordinate1[0] == coordinate2[0]:
        if int(coordinate1[1]) > int(coordinate2[1]):
            line = [coordinate1[0] +','+ coordinate1[1]]
            for i in range(0,int(coordinate1[1])-int(coordinate2[1])):
                line.append('{},{}'.format(int(coordinate1[0]),int(coordinate1[1])-1-i))
        if int(coordinate1[1]) < int(coordinate2[1]):
            line = [coordinate1[0] +','+ coordinate1[1]]
            for i in range(0,abs(int(coordinate1[1])-int(coordinate2[1]))):
                line.append('{},{}'.format(int(coordinate1[0]),int(coordinate1[1])+1+i))

    if coordinate1[1] == coordinate2[1]:
        if int(coordinate1[0]) > int(coordinate2[0]):
            line = [coordinate1[0] +','+ coordinate1[1]]
            for i in range(0,int(coordinate1[0])-int(coordinate2[0])):
                line.append('{},{}'.format(int(coordinate1[0])-1-i,int(coordinate1[1])))
        if int(coordinate1[0]) < int(coordinate2[0]):
            line = [coordinate1[0] +','+ coordinate1[1]]
            for i in range(0,abs(int(coordinate1[0])-int(coordinate2[0]))):
                line.append('{},{}'.format(int(coordinate1[0])+1+i,int(coordinate1[1])))
    # print(line)
    # print(coordinates)
    return line

def part2(data):
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for i in range(0,1000):
        for j in range(0,1000):
            grid[i][j] = "{},{}".format(i, j)
    intersect=0
    for i in range(len(data)):
        line = makeLine2(data[i])
        if len(line)>0:
            for i in range(len(line)):
                coordinate = line[i].split(',')
                if grid[int(coordinate[0])][int(coordinate[1])] =='x':
                    intersect+=1
                    grid[int(coordinate[0])][int(coordinate[1])] ='L'
                if grid[int(coordinate[0])][int(coordinate[1])] !='x' and grid[int(coordinate[0])][int(coordinate[1])] !='L':
                    grid[int(coordinate[0])][int(coordinate[1])] ='x'
                
    return intersect

def makeLine2(coordinates):
    splittedCoordinates = coordinates.split('->')
    coordinate1 = splittedCoordinates[0].replace(' ','').split(',')
    coordinate2 = splittedCoordinates[1].replace(' ','').split(',')
    line = []
    if coordinate1[0] == coordinate2[0]:
        if int(coordinate1[1]) > int(coordinate2[1]):
            line = [coordinate1[0] +','+ coordinate1[1]]
            for i in range(0,int(coordinate1[1])-int(coordinate2[1])):
                line.append('{},{}'.format(int(coordinate1[0]),int(coordinate1[1])-1-i))
        if int(coordinate1[1]) < int(coordinate2[1]):
            line = [coordinate1[0] +','+ coordinate1[1]]
            for i in range(0,abs(int(coordinate1[1])-int(coordinate2[1]))):
                line.append('{},{}'.format(int(coordinate1[0]),int(coordinate1[1])+1+i))

    if coordinate1[1] == coordinate2[1]:
        if int(coordinate1[0]) > int(coordinate2[0]):
            line = [coordinate1[0] +','+ coordinate1[1]]
            for i in range(0,int(coordinate1[0])-int(coordinate2[0])):
                line.append('{},{}'.format(int(coordinate1[0])-1-i,int(coordinate1[1])))
        if int(coordinate1[0]) < int(coordinate2[0]):
            line = [coordinate1[0] +','+ coordinate1[1]]
            for i in range(0,abs(int(coordinate1[0])-int(coordinate2[0]))):
                line.append('{},{}'.format(int(coordinate1[0])+1+i,int(coordinate1[1])))
    
    if int(coordinate1[0]) < int(coordinate2[0]) and coordinate1[1] != coordinate2[1]:
        # line=[splittedCoordinates[0]]
        line = []
        if int(coordinate1[1]) > int(coordinate2[1]):
            xcoordinates = [int(coordinate1[0])]
            ycoordinates = [int(coordinate1[1])]
            for i in range(0,abs(int(coordinate1[0])-int(coordinate2[0]))):
                xcoordinates.append(int(coordinate1[0])+1+i)
            for i in range(0,abs(int(coordinate1[1])-int(coordinate2[1]))):
                ycoordinates.append(int(coordinate1[1])-1-i)
            for i in range(len(xcoordinates)):
                line.append('{},{}'.format(xcoordinates[i],ycoordinates[i]))
        if int(coordinate1[1]) < int(coordinate2[1]):
            xcoordinates = [int(coordinate1[0])]
            ycoordinates = [int(coordinate1[1])]
            for i in range(0,abs(int(coordinate1[0])-int(coordinate2[0]))):
                xcoordinates.append(int(coordinate1[0])+1+i)
            for i in range(0,abs(int(coordinate1[1])-int(coordinate2[1]))):
                ycoordinates.append(int(coordinate1[1])+1+i)
            for i in range(len(xcoordinates)):
                line.append('{},{}'.format(xcoordinates[i],ycoordinates[i]))

    if int(coordinate1[0]) > int(coordinate2[0]) and coordinate1[1] != coordinate2[1]:
        # line=[splittedCoordinates[0]]
        line = []
        if int(coordinate1[1]) > int(coordinate2[1]):
            xcoordinates = [int(coordinate1[0])]
            ycoordinates = [int(coordinate1[1])]
            for i in range(0,abs(int(coordinate1[0])-int(coordinate2[0]))):
                xcoordinates.append(int(coordinate1[0])-1-i)
            for i in range(0,abs(int(coordinate1[1])-int(coordinate2[1]))):
                ycoordinates.append(int(coordinate1[1])-1-i)
            for i in range(len(xcoordinates)):
                line.append('{},{}'.format(xcoordinates[i],ycoordinates[i]))
        if int(coordinate1[1]) < int(coordinate2[1]):
            xcoordinates = [int(coordinate1[0])]
            ycoordinates = [int(coordinate1[1])]
            for i in range(0,abs(int(coordinate1[0])-int(coordinate2[0]))):
                xcoordinates.append(int(coordinate1[0])-1-i)
            for i in range(0,abs(int(coordinate1[1])-int(coordinate2[1]))):
                ycoordinates.append(int(coordinate1[1])+1+i)
            for i in range(len(xcoordinates)):
                line.append('{},{}'.format(xcoordinates[i],ycoordinates[i]))
    return line
            
def main():
    data = getData()
    answer1 = part1(data)
    print(answer1)

    answer2 =part2(data)
    print(answer2)

main()