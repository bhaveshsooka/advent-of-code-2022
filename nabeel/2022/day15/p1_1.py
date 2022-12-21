import sys
import cmath
import math
import re

row_dict = {
    '1.in':10,
    '2.in':2_000_000
}

def lprint(lst):
    print(*lst, sep='\n')

file = sys.argv[1] if len(sys.argv)>1 else '0.in'
lines = open(file).readlines()
row = row_dict[file]

def distance(a:complex,b:complex):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag)) 

def sensor_range(r:dict, row:int):
    s = r['sensor']
    d = r['distance']
    d_z = complex(d,d)
    b_min = s-d_z
    b_max = s+d_z
    # print(b_min)
    # print(b_max)
    block_list = []
    if int(b_min.imag)<=row<=int(b_max.imag):
        for r in range(int(b_min.real),int(b_max.real)+1):
            z = complex(r,row)
            no_beacon = distance(s,z)<=d
            if no_beacon:
                block_list.append(z)
            # print(z, no_beacon)
    return block_list

def analytical(r:dict, row:int):
    print(r)
    s = r['sensor']
    b = r['beacon']
    d = r['distance']
    adjust = 0
    if s.imag==row:
        print('sensor in row')
        adjust -= 1
    if b.imag == row:
        print('beacon in row')
        adjust -= 1

    y_min = int(s.imag-d)    
    y_max = int(s.imag+d)

    d_z = complex(d,0)
    z = s-d_z
    if row not in range(y_min,y_max+1):
        # print('row not in y range')
        return {
            'min': None,
            'max': None,
            'adjust':adjust}
    if s.imag == row:
        # print('sensor on row')
        return {
            'min': s.real - d,
            'max': s.real + d,
            'adjust':adjust}
    if row in [y_min, y_max]:
        # print('row at y max or y min')
        return {
            'min': s.real,
            'max': s.real,
            'adjust':adjust}
    if s.imag > row:
        # print('row intersects below sensor')
        c = int(z.imag+z.real)#-ve below
        x = c-row
    if s.imag < row:
        # print('row intersects above sensor')
        c = int(z.imag-z.real)#+ve above
        x = row-c

    min_range = x
    max_range = int(s.real) + int(abs(s.real - min_range))
    print(f'col {min_range} -> {max_range}')
    return {
        'min': min_range,
        'max': max_range,
        'adjust':adjust}

def parse(line:str):
    n = re.findall('[-+]?[\d]+', line)
    n = [int(i) for i in n]
    # n = list(map(int,n))
    r = {
        'sensor': complex(n[0],n[1]), 
        'beacon': complex(n[2],n[3])
    }
    r['distance'] = distance(r['sensor'],r['beacon'])
    r['block'] = analytical(r, row)
    return r

pairs = [parse(line) for line in lines]
# lprint(pairs)

mins = [pair['block']['min'] for pair in pairs if pair['block']['min'] is not None]
print(f'mins: {mins}')
maxs = [pair['block']['max'] for pair in pairs if pair['block']['max'] is not None]
print(f'maxs: {maxs}')

mm = zip(mins,maxs)
mm = list(mm)
print(mm)

def first(item):
    return item[0]
mm = sorted(mm,key=first)
print(mm)

mm_min = mm[0]
empty_range = []
c_min, c_max = mm_min
for pair in mm[1:]:
    p_min, p_max = pair
    if p_min <= c_max:
        if p_max <= c_max:
            continue
        c_max = p_max
    if p_min > c_max:
        empty_range.append((c_min,c_max))
        c_min, c_max = pair
    print(pair, '->', c_min, c_max)

empty_range.append((c_min,c_max))

print(empty_range)
difs = [pair[1]-pair[0] for pair in empty_range]
print(sum(difs))
# min_range = min(mins)
# min_sort = sorted(mins)
# print(f'min sorted: {min_sort}')
# for min_item in min_sort:
#     idx = mins.index(min_item)
#     max_item = maxs[idx]
#     print(f'{idx}: {min_item}->{max_item}')

adjs = [pair['block']['adjust'] for pair in pairs]
print(f'adjs: {adjs}')
