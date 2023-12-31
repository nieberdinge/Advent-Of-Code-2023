import re 

f = open('day3/day3.txt')
total = 0

engine = f.readlines()

def isValid(line, start, stop):
    if line < 0 or line >= len(engine):
        return False
    if start < 0:
        start+=1
    if stop >= len(engine[line]):
        stop-=1

    sub = engine[line][start:stop]
    sub = re.sub(r"\.","", sub)
    sub = re.sub(r"\d","", sub)

    # check if gear box 
    # if so, find index
    
    if len(sub) > 0:
        return True
    return False

def isSpecial(index, line):
    if index < 0 or index >= len(line):
        return False
    letter = line[index]
    sub = re.sub(r"\.","", letter)
    sub = re.sub(r"\d","", sub)
    if len(sub) > 0:
        return True
    return False


for x in range(len(engine)):
    line = engine[x].strip()
    for number in re.finditer("\d+", line):
        # print("Number:",engine[x][number.start():number.end()])
        before = isValid(x-1, number.start()-1, number.end()+1)
        after = isValid(x+1, number.start()-1, number.end()+1)
        left = isSpecial(number.start()-1, line)
        right = isSpecial(number.end(), line)
        if before or after or left or right:
            total += int(engine[x][number.start():number.end()])


# check if it is a gear box
# if so, dict<string "x+y", list[]>
# at the end check if list == 2
print("Part 1 is:", total)
f.close()