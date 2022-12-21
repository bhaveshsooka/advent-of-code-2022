import sys
import cmath
import math
import re
from tqdm import tqdm
import json 

rr = {
    '1.in':(0,20),
    '2.in':(0,4_000_000)
}

def inbounds(step:tuple):
    br = rr[file]
    x,y = step
    if br[0]<=x<=br[1] and br[0]<=y<=br[1]:
        return True
    return False

def lprint(lst):
    for item in lst:
        print(json.dumps(item, indent=2, default=str))

file = sys.argv[1] if len(sys.argv)>1 else '0.in'
lines = open(file).readlines()

def distance(a:complex,b:complex):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag)) 

def distanceStep(a:tuple,b:complex):
    a_real, a_imag = a
    return int(abs(a_real - b.real) + abs(a_imag - b.imag)) 

def outline(SF:'tuple(complex)', direction:int):
    S,F = SF
    path = zip(range(int(S.real),int(F.real+1)), range(int(S.imag),int(F.imag+1*direction),direction))
    return path


def parse(line:str):
    n = re.findall('[-+]?[\d]+', line)
    n = [int(i) for i in n]
    # n = list(map(int,n))
    r = {
        'sensor': complex(n[0],n[1]), 
        'beacon': complex(n[2],n[3])
    }
    r['distance'] = distance(r['sensor'],r['beacon'])
    r['W'] = r['sensor']+complex(0,r['distance']+1)
    r['A'] = r['sensor']-complex(r['distance']+1,0)
    r['S'] = r['sensor']-complex(0,r['distance']+1)
    r['D'] = r['sensor']+complex(r['distance']+1,0)
    r['AW'] = outline((r['A'],r['W']),1)
    r['SD'] = outline((r['S'],r['D']),1)
    r['AS'] = outline((r['A'],r['S']),-1)
    r['WD'] = outline((r['W'],r['D']),-1)
    return r

pairs = [parse(line) for line in lines]

def dist_sort(item):
    return item['distance']
pairs = sorted(pairs, key=dist_sort, reverse=True)
lprint(pairs)

def checkPairOutlines():
    for pair in tqdm(pairs):
        for path in ['AW','SD','AS','WD']:
            for step in pair[path]:
                if inbounds(step):
                    for pair in pairs:
                        if distanceStep(step, pair['sensor']) <= pair['distance']:
                            break
                        if pair == pairs[-1]:
                            print(step)
                            return step

step = checkPairOutlines()
solution = step[0]*4_000_000+step[1]
print(solution)
