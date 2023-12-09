f = open('day8/day8.txt')
lines = f.readlines()
f.close()

class Node():
    def __init__(self, key, left, right) -> None:
        self.left = left
        self.right = right
        self.key = key

map = {}

instructions = lines.pop(0).strip()
lines.pop(0)

for line in lines:
    map[line[:3]] = Node(line[:3], line[7:10], line[12:15])

# Day 1

index = 0
curr = map['AAA']
count = 0
while (curr.key != 'ZZZ'):
    if instructions[index] == 'L':
        curr = map[curr.left]
    else:
        curr = map[curr.right]
    count += 1
    index += 1
    if index == len(instructions):
        index = 0
print("Day 1", count)

# Day 2

# allEndingWithA = [loc for loc in list(map) if loc[2] == 'A']
# index = 0
# count = 0

# def isAllZ():
#     for loc in allEndingWithA:
#         if loc[2] != 'Z':
#             return False
#     return True

# while (not isAllZ()):
#     for x in range(len(allEndingWithA)):
#         curr = map[allEndingWithA[x]]
#         if instructions[index] == 'L':
#             allEndingWithA[x] = map[curr.left].key
#         else:
#             allEndingWithA[x] = map[curr.right].key
#     count += 1
#     index += 1
#     if index == len(instructions):
#         index = 0

# print("day 2:", count)


# Cheating with solution found online
import math
import numpy as np

def findPath(start: str):
    index = 0
    curr = map[start]
    count = 0
    while (curr.key[2] != 'Z'):
        if instructions[index] == 'L':
            curr = map[curr.left]
        else:
            curr = map[curr.right]
        count += 1
        index += 1
        if index == len(instructions):
            index = 0
    return count

numbers = [findPath(loc) for loc in list(map) if loc[2] == 'A']
print("Day 2 with math", np.lcm.reduce(numbers))