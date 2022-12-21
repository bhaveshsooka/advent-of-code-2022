import sys
import cmath
import math
import re

rr = {
    '1.in':(0,20),
    '2.in':(2_000_000,4_000_000)
}

def lprint(lst):
    print(*lst, sep='\n')

file = sys.argv[1] if len(sys.argv)>1 else '0.in'
lines = open(file).readlines()
br = rr[file]

def distance(a:complex,b:complex):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag)) 

def parse(line:str):
    n = re.findall('[-+]?[\d]+', line)
    n = [int(i) for i in n]
    # n = list(map(int,n))
    r = {
        'sensor': complex(n[0],n[1]), 
        'beacon': complex(n[2],n[3])
    }
    r['distance'] = distance(r['sensor'],r['beacon'])
    return r

pairs = [parse(line) for line in lines]

def dist_sort(item):
    return item['distance']
pairs = sorted(pairs, key=dist_sort, reverse=True)
lprint(pairs)

sensors = [pair['sensor'] for pair in pairs]
beacons = [pair['beacon'] for pair in pairs]
distances = [pair['distance'] for pair in pairs]

found = False
for irow in range(br[0],br[1]+1):
    for icol in range(br[0],br[1]+1):
        # print(irow, icol)
        z = complex(irow,icol)
        # print(f'idx: {z}')
        i = 0
        for sensor in range(len(sensors)):
            dist = distance(sensors[sensor],z)
            # print(dist, distances[sensor])
            if dist<=distances[sensor]:
                # print(f'within sensor {sensor} range of {distances[sensor]}')
                break
            i += 1
        if i == len(sensors):
            found = True
            break
    if irow%1000 == 0:
        print(irow)
    if found:
        break


print(f'idx: {z}')
freq = z.real*4_000_000 + z.imag
print(f'tuning freq: {freq}')


a = set([1,2,3])
print(a)
print(a.add(1))
print(a.add(4))
print(a)
