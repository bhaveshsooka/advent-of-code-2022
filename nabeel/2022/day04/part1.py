from textwrap import wrap
input = open('test.txt', 'r')
# input = open('input.txt', 'r')
lines = input.readlines()
output = open('output.txt', 'w')

# print(lines)

total = 0
for line in lines:
    inside = ''
    pairs = line.strip().split(',')
    num_pairs = [pair.split('-') for pair in pairs]
    nums = [int(num) for pair in num_pairs for num in pair]
    numrange = f'{min(nums)}-{max(nums)}'
    if numrange in pairs: 
        total+=1
        inside = '*'
    print(inside, pairs, numrange)

print(total)
