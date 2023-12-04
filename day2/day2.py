f = open('day2/day2.txt')

totals = {"red": 12, "green": 13, "blue": 14}

total = 0
powerSets = 0
for game in f.readlines():
    gameNum = game.split(':')[0].split(' ')[1]
    rounds = game.split(':')[1].strip().split(';')
    minTotal = {"red": 1, "green": 1, "blue": 1}
    hasError = False
    for round in rounds:
        for pull in round.strip().split(','):
            num = int(pull.strip().split(' ')[0])
            name = pull.strip().split(' ')[1]
            if totals[name] < num:
                hasError = True
            if minTotal[name] < num:
                minTotal[name] = num
    if hasError == False:
        total += int(gameNum)
    powerSets += minTotal["red"] * minTotal["blue"] * minTotal["green"]

print("The total is", total)        
print("powerSets", powerSets)