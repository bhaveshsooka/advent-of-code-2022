# input = open('test.txt', 'r')
input = open('input.txt', 'r')
lines = input.readlines()
output = open('output.txt', 'w')

print(lines)

themDict = {
    'A':0,
    'B':1,
    'C':2
}

resultDict = {
    'X':0,
    'Y':1,
    'Z':2
}

selectedDict = {
    'A':1,
    'B':2,
    'C':3
}

meRoundTable = [
    'CAB',
    'ABC',
    'BCA'
]

roundDict = {
    'X':0,
    'Y':3,
    'Z':6
}

total = 0
for line in lines:
    [them, result] = line.strip().split()
    print(them, result, '->', meRoundTable[themDict[them]][resultDict[result]])
    total += roundDict[result] + selectedDict[meRoundTable[themDict[them]][resultDict[result]]]
print(total)
