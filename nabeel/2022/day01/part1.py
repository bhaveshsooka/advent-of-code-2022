input = open('test.txt', 'r')
# input = open('input.txt', 'r')
lines = input.readlines()
output = open('output.txt', 'w')

total = 0
max = 0
for line in lines:
    if line == '\n':
        if total > max:
            max = total
        output.write(f'\t\t {max}\n')
        total = 0
    else:
        number = int(line)
        total += number
        output.write(f'{number}\t\t{total}\n')

    
print(max)
