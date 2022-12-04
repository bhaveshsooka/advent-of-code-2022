from textwrap import wrap
# input = open('test.txt', 'r')
input = open('input.txt', 'r')
lines = input.readlines()
output = open('output.txt', 'w')

# print(lines)
pairA_min = 0
pairA_max = 1
pairB_min = 2
pairB_max = 3


total = 0
for line in lines:
    inside = '*'
    pairs = line.strip().split(',')
    pairs = [pair.split('-') for pair in pairs]
    nums = [int(num) for pair in pairs for num in pair]
    if nums[pairA_max]<nums[pairB_min] or nums[pairA_min]>nums[pairB_max]: 
        inside = ''
    else:
        total += 1
    print(inside, pairs, nums)

print(total)
