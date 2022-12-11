import numpy as np
import json

file = 'test1'
# file = 'test2'
# file = 'test3'

in_file = open(file)
lines = in_file.readlines()

lines = [line.strip().split() for line in lines if len(line)>1]
# print(*lines, sep='\n')

info_length = 6
num_monkeys = int(len(lines)/info_length)
print('Monkeys: ',num_monkeys)

monkeys = {}
for monkey in range(num_monkeys):
    info = lines[monkey*info_length:(monkey+1)*info_length]
    print(*info,sep='\n')
    name = info[0][1].strip(':')
    monkeys[name] = {}
    items = [int(item.strip(",")) for item in info[1][2:]] 
    print('items:',*items)
    monkeys[name]['items']=items
    monkeys[name]['total']=0
    operation = ' '.join(info[2][1:])
    monkeys[name]['operation']=operation
    print('operation',operation)
    test = int(info[3][-1])
    monkeys[name]['test']=test
    new = 0
    for old in items:
        exec(operation) # new = ??????
        case = round(new/3)%test == 0
        print(new, case)
    monkeys[name]['true'] = info[4][-1]
    monkeys[name]['false'] = info[5][-1]
    print(10*"=")

# monkeys_dict = json.dumps(monkeys, indent=2)
# print(monkeys_dict)

for round in range(20):
    # print(f'round : {round+1}')
    for key in monkeys.keys():
        monkey = monkeys[key]
        # print(key)
        for old in monkey['items']:
            exec(monkey['operation']) # new = ??????
            change = int(new/3)
            case = change%(monkey['test']) == 0
            if case: 
                monkeys[monkey['true']]['items'].append(change)
                move = f"{change}-> monkey {monkey['true']}"
            else: 
                monkeys[monkey['false']]['items'].append(change)
                move = f"{change}-> monkey {monkey['false']}"
            # print(f"{old} -> {new} -> {change} {case} -> {move}")
        monkey['total'] += len(monkey['items'])
        monkey['items'] = []
        # print(10*'=')

    # [print(*monkeys[name]['items']) for name in monkeys.keys()]
    # print(10*'#')

activity = [print(name, monkeys[name]['total']) for name in monkeys.keys()]
