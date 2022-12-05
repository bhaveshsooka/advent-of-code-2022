import re
# input = open('test.txt', 'r')
input = open('input.txt', 'r')
lines = input.readlines()
output = open('output.txt', 'w')

split = lines.index('\n')
stacks = lines[:split]
print('Split it')
[print(line) for line in stacks]
stack_index = stacks[-1]
stack_num = int(max(stack_index))
crate_idx = [stack_index.index(str(idx)) for idx in range(1,stack_num+1)]
print(crate_idx)
stack_lists = [[] for _ in range(stack_num+1)]
print("===============")
print('Flip it')
reverse_stack = stacks[-2::-1]
# [print(line) for line in reverse_stack]
print(*reverse_stack)
stack_length = len(reverse_stack)
print('Reverse it')
[stack_lists[num+1].append(reverse_stack[row][crate_idx[num]]) for row in range(stack_length) for num in range(stack_num) if reverse_stack[row][crate_idx[num]] != ' ']
print(stack_lists)

# trans_stack = [[] for _ in range(len(reverse_stack[0]))]
# for row in range(len(reverse_stack)): 
#     for col in range(len(reverse_stack[0])):
#         if col in crate_idx and reverse_stack[row][col]!=' ':
#             trans_stack[col].append(reverse_stack[row][col])

# trans_stack = [trans_stack[i] for i in range(len(trans_stack)) if i in crate_idx]
# [print(stack) for stack in trans_stack]
print('Move it')
moves = lines[split+1:]
moves_idx = [re.findall(r'[0-9]+', move) for move in moves]

def updown(stacks, fromstack, tostack):
    crate = stacks[int(fromstack)].pop()
    stacks[int(tostack)].append(crate)
    return stacks

reps = 0
fromidx = 1
toidx = 2
for move in moves_idx:
    # print(move)
    for _ in range(int(move[reps])):
        stack_lists = updown(stack_lists, move[fromidx], move[toidx])

[print(stack) for stack in stack_lists]

print('Merge it')
solution = [stack[-1] for stack in stack_lists if len(stack)>0]
print(str(solution))
