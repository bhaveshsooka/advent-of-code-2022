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

meDict = {
    'X':0,
    'Y':1,
    'Z':2
}

selectedDict = {
    'X':1,
    'Y':2,
    'Z':3
}

roundTable = [
    [3,6,0],
    [0,3,6],
    [6,0,3]
]

total = 0
for line in lines:
    [them, me] = line.strip().split()
    print(them, me, '->', roundTable[themDict[them]][meDict[me]], '+', selectedDict[me])
    total +=  roundTable[themDict[them]][meDict[me]]+ selectedDict[me]

print(total)
