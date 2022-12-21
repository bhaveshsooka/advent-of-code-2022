import sys
import cmath
import math
import re
from tqdm import tqdm

rr = {
    '1.in':(0,20),
    '2.in':(0,4_000_000)
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
    # r['block'] = sensor_range(r, row)
    return r

pairs = [parse(line) for line in lines]
def dist_sort(item):
    return item['distance']
pairs = sorted(pairs, key=dist_sort, reverse=True)
lprint(pairs)

empty_set = set()

def sensor_range(r:dict):
    s = r['sensor']
    d = r['distance']
    d_z = complex(d,d)
    b_min = s-d_z
    b_max = s+d_z
    for r in range(int(b_min.real),int(b_max.real)+1):
        if br[0]<=r<=br[1]:
            if r%100_000==0: print(r)
            for c in tqdm(range(int(b_min.imag),int(b_max.imag)+1),):
                if br[0]<=c<=br[1]:
                    z = complex(r,c)
                    if z not in empty_set:
                        no_beacon = distance(s,z)<=d
                        if no_beacon:
                            empty_set.add(z)
                        # print(z, no_beacon)

print('filling range')
for i,pair in enumerate(pairs):
    print(f'sensor {i}')
    sensor_range(pair)

print(len(empty_set))

def find_missing():
    for row in range(br[0], br[1]):
        for col in range(br[0], br[1]):
            if complex(row,col) not in empty_set:
                return (row,col)

print(find_missing())


