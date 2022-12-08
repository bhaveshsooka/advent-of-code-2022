import re
input = open('test.txt', 'r')
# input = open('input.txt', 'r')
lines = input.readlines()
# output = open('output.txt', 'w')
lines = [line.strip() for line in lines]
# print(*lines, sep='\n')
# [print(idx, line) for idx,line in enumerate(lines)]

commands = [idx for idx,line in enumerate(lines) if '$' in line]
commands.append(len(lines))
print(commands)

for idx in range(len(commands)-1):
    print(lines[commands[idx]:commands[idx+1]])

{}
{'/':{}}
