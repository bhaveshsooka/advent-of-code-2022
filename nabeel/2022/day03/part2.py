from textwrap import wrap
# input = open('test.txt', 'r')
input = open('input.txt', 'r')
lines = input.readlines()
output = open('output.txt', 'w')

# print(lines)
rank = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0

linenum = len(lines)
groupsize = 3
groups = int(linenum/groupsize)
print(groups)
for idx in range(groups):
    group = lines[idx*groupsize:(idx+1)*groupsize]
    group = [set(line.strip()) for line in group]
    letter = list(set.intersection(*group))[0]
    total += rank.index(letter)

print(total)
