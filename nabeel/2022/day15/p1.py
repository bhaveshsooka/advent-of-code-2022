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
    if s.imag < row:
        # print('row intersects below sensor')
        c = int(z.imag+z.real)#-ve below
        x = c-row
    if s.imag > row:
        # print('row intersects above sensor')
        c = int(z.imag-z.real)#+ve above
        x = row-c

    min_range = x
    max_range = int(s.real) + int(abs(s.real - min_range))
    print(f'row {min_range} -> {max_range}')
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
    r['block'] = sensor_range(r, row)
    return r

pairs = [parse(line) for line in lines]
# lprint(pairs)

blocks = [coord for pair in pairs for coord in pair['block'] if int(coord.imag) == row]
sensors = [pair['sensor'] for pair in pairs  if int(pair['sensor'].imag) == row]
beacons = [pair['beacon'] for pair in pairs  if int(pair['beacon'].imag) == row]

blocks = set(blocks)-set(sensors)-set(beacons)
print(len(blocks))

# mins = [pair['block']['min'] for pair in pairs if pair['block']['min'] is not None]
# print(f'mins: {mins}')
# maxs = [pair['block']['max'] for pair in pairs if pair['block']['max'] is not None]
# print(f'maxs: {maxs}')

# mm = zip(mins,maxs)
# mm = list(mm)
# mx = [a*b for a,b in mm]
# print(mx)
# min_range = min(mins)
# min_sort = sorted(mins)
# print(f'min sorted: {min_sort}')
# for min_item in min_sort:
#     idx = mins.index(min_item)
#     max_item = maxs[idx]
#     print(f'{idx}: {min_item}->{max_item}')
