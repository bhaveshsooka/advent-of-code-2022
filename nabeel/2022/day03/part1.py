from textwrap import wrap
# input = open('test.txt', 'r')
input = open('input.txt', 'r')
lines = input.readlines()
output = open('output.txt', 'w')

# print(lines)
rank = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
for line in lines:
    line = line.strip()
    half = int(len(line)/2)
    a,b = line[:half], line[half:]
    letter = list(set(a)&set(b))[0]
    total += rank.index(letter)

print(total)
