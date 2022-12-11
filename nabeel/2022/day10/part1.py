import numpy as np

file = 'test1'
file = 'test2'
file = 'test3'

in_file = open(file)
lines = in_file.readlines()

def parse(line):
    if len(line) == 1: return (line[0], 0)
    return (line[0], int(line[1]))
lines = [parse(line.strip().split()) for line in lines]
print(*lines, sep='\n')

register = [1]

for line in lines:

    operation = line[0]
    value = line[1]

    if operation == 'noop':
        register.append(register[-1])
    
    if operation == 'addx':
        register.append(register[-1])
        register.append(register[-1]+value)



# print(*zip(range(len(register)), register))
signal_strengths = []
for idx in [20,60,100,140,180,220]:
    print(idx, register[idx-1])
    strength = idx * register[idx-1]
    signal_strengths.append(strength)

print(sum(signal_strengths))
