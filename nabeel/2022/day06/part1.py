import re
input = open('test.txt', 'r')
# input = open('input.txt', 'r')
lines = input.readlines()
output = open('output.txt', 'w')
lines = [line.strip() for line in lines]
# print(*lines, sep='\n')

buffer = 4

for line in lines:
    print(line)
    for idx in range(len(line)):
        sline = line[idx:buffer+idx]
        sline_set = set(sline)
        sline_set_len = len(sline_set)
        if sline_set_len == buffer:
            print(f'{idx*" "+sline}|{idx+buffer}')
            break
        else:
            print(f'{idx*" "+sline}')
