f = open('day6/day6.txt')
lines = f.readlines()

numbers = list(filter(None,lines[0].strip().split(' ')))[1:]
distance = list(filter(None,lines[1].strip().split(' ')))[1:]

total = 1
for x in range(len(numbers)):
    total *= len([num for num in range(1, int(numbers[x])) if (int(numbers[x]) - num) * num > int(distance[x])])

print(total)

