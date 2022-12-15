import sys
from functools import cmp_to_key
import math

file = sys.argv[1] if len(sys.argv)>1 else '0.in'
lines = open(file).readlines()
lines = [line.strip() for line in lines if len(line)>1]
# print(*lines, sep='\n')

def LvR(left, right,tab=0):

    print(tab*'\t',f'Compare {left} vs {right}')

    for list_idx in range(len(left)):
        l = left[list_idx]
        try:
            r = right[list_idx]
        except:
            print(tab*'\t','Right side ran out of items, so inputs are in the wrong order')
            return 1
        print(tab*'\t',f'Compare {left[list_idx]} vs {right[list_idx]}')

        if type(l) == int and type(r) == int:
            if l<r : 
                print(tab*'\t',"Left side is smaller, so inputs are in the right order")
                return -1
            if l>r : 
                print(tab*'\t','Right side is smaller, so inputs are in the wrong order')
                return 1
            if l==r: continue
        
        if type(l) == list and type(r) == list:
            decision = LvR(l,r,tab+1)
            if decision != 0:
                return decision
            
        if type(l) == int:
            print(tab*'\t',f'Mixed types; convert left to {[l]} and retry comparison')
            decision = LvR([l],r, tab+1)
            if decision != 0:
                return decision

        if type(r) == int:
            print(tab*'\t',f'Mixed types; convert right to {[r]} and retry comparison')
            decision = LvR(l,[r], tab+1)
            if decision != 0:
                return decision
    if len(left)<len(right):
        print(tab*'\t','Left side ran out of items, so inputs are in the right order')
        return -1
    print(tab*'\t','Lists are identical, check next input')
    return 0

pkts = [[[2]],[[6]]]

for line in lines:
    item = 'error'
    exec(f'item = {line}')
    pkts.append(item)

pkts_sort = sorted(pkts, key=cmp_to_key(LvR))
print(*pkts_sort, sep='\n')

a = pkts_sort.index([[2]])+1
b = pkts_sort.index([[6]])+1
print(a*b)
