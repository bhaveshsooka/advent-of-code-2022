# input = open('test.txt', 'r')
input = open('input.txt', 'r')
lines = input.readlines()
lines.append('\n')
output = open('output.txt', 'w')

total = 0
maxes = [0,0,0]
for line in lines:
    if line == '\n':
        if total > min(maxes):
            maxes.append(total)
            maxes.sort()
            maxes = maxes[1:]
        output.write(f'{maxes}\n')
        total = 0
    else:
        number = int(line)
        total += number
        output.write(f'{number}\t\t{total}\n')

    
print(maxes)
print(sum(maxes))
