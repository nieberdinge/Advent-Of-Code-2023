import re

numbers = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9"]
conversion = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

f = open('day1.txt')

total = 0
for line in f.readlines():
    word = line.strip()
    min = 100000
    max = 0
    minNumber = ""
    maxNumber = ""
    for number in numbers:
        for index in re.finditer(number, word):
            if index.start() > max:
                max = index.start()
                maxNumber = conversion[number] if number in conversion else number
            if index.start() < min:
                min = index.start()
                minNumber = conversion[number] if number in conversion else number

    total += int(minNumber + maxNumber)

print("Your total is", total)

f.close()