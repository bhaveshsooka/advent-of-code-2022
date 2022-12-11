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
# print(*lines, sep='\n')

op_num = 0
register_during = [1]
register_end = [1]
skip = False
for cycle in range(1,240+1):
    print('cycle',cycle)
    # start
    print(f'\tskip start: {bool(skip)}')
    if not skip and op_num<len(lines):
        start_op = lines[op_num]
        operation = start_op[0]
        value = start_op[1]

        if operation == 'noop':
            skip = 1

        if operation == 'addx':
            skip = 2

    # during
    register_during.append(register_end[-1])
    skip -= 1

    # end
    print(f'\tskip end: {bool(skip)}')
    register_end.append(register_during[-1])
    if not skip and op_num < len(lines):
        if operation == 'addx':
            register_end[-1] = register_during[-1] + value
            print(f'updated register to {register_end[-1]}')
        op_num += 1
    # print(f'register at end: {register_end[-1]} of {len(register_end)} items')

# print('Cycle During End', *zip(range(1,len(register_during)+1), register_during[1:], register_end[1:]), sep='\n')

# print(20*'=')

# print(len(register_during))
# print(len(register_end))

sprite_span = 1
output = []
print('cycle', 'pos', 'spr', 'dur', 'dif', 'draw')
for cycle in range(1,240+1):
    CRT = cycle - 1
    sprite = CRT%40
    dif = abs(sprite-register_during[cycle])
    show = ' '
    if dif <= sprite_span: show='#'
    print(f'{cycle:<5}', f'{CRT:<3}', f'{sprite:<3}', f'{register_during[cycle]:<3}', f'{dif:<3}',show)
    output.append(show)

print(len(output))

picture = []
for row in range(6):
    r = output[row*40:(row+1)*40]
    picture.append(''.join(r))

print(*picture,sep='\n')
