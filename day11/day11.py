from copy import deepcopy
import re
f = open('day11/day11.txt')
lines = f.readlines()
f.close()

lines = [line.strip() for line in lines]
starMap = deepcopy(lines)

num = 0
for line in range(len(lines)):
    if '#' not in lines[line]:
        starMap.insert(line+num, lines[line])
        num += 1

def hasGalaxyInCol(col):
    for line in starMap:
        if line[col] == '#':
            return True
    return False

noGalaxy = []
for col in range(len(starMap[0])):
    if(not hasGalaxyInCol(col)):
        noGalaxy.append(col)
num = 0
for col in noGalaxy:
    for line in range(len(starMap)):
        starMap[line] = starMap[line][:(col + num)] + '.' + starMap[line][(col + num):]
    num += 1


coords = []
for line in range(len(starMap)):
    coords.extend([(line, m.start(),) for m in re.finditer('#', starMap[line])])

total = 0
for coord1 in coords:
    for coord2 in coords:
        total += abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

print(total)