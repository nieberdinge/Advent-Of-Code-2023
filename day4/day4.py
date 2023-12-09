f = open('day4/day4.txt')
lines = f.readlines()
total = 0
currCard = 1
count = {1:1}

def addToCount(num, multiplier):
    if num > len(lines):
        return
    if num not in count:
         count.update({num: 1+multiplier})
    count[num] += multiplier
            

for line in lines:
    if currCard not in count:
        count.update({currCard: 1})
    numbers = line.strip().split(':')[1]
    lottery = list(filter(None, numbers.strip().split('|')[0].strip().split(' ')))
    yours = list(filter(None, numbers.strip().split('|')[1].strip().split(' ')))
    winningNums = [num for num in yours if num in lottery]
    total += 2 ** (len(winningNums)-1) if len(winningNums) > 0 else 0
    for x in range(0,len(winningNums)):
            addToCount(currCard+x+1, count[currCard])
    currCard +=1

total2 = sum(count.values())
print("The total is:", total)
print("The total2 is:", total2)

    