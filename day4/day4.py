f = open('day4/day4.txt')

total = 0

for line in f.readlines():
    numbers = line.strip().split(':')[1]
    lottery = list(filter(None, numbers.strip().split('|')[0].strip().split(' ')))
    yours = list(filter(None, numbers.strip().split('|')[1].strip().split(' ')))
    winningNums = [num for num in yours if num in lottery]
    total += 2 ** (len(winningNums)-1) if len(winningNums) > 0 else 0

print("The total is:", total)
    