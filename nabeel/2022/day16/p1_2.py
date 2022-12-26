import sys
import math
import json
from copy import deepcopy

def jprint(obj):
    print(json.dumps(obj, indent=2))

def lprint(lst,inverse=False):
    if inverse:
        print(*lst[::-1], sep='\n')
    else:
        print(*lst, sep='\n')

file = sys.argv[1] if len(sys.argv)>1 else '0.in'
lines = open(file).readlines()
lines = [line.strip() for line in lines]

info = {}

for line in lines:
    VT = line.split(';')
    V = VT[0].split()
    info[V[1]]={}
    info[V[1]]['rate'] = int(V[-1].split('=')[-1])
    newValves = [tunnel.strip(',') for tunnel in VT[1].split()[4:]]
    newValves.sort()
    info[V[1]]['paths'] = newValves

jprint(info)

def best_path(at_valve, open_valves, minutes, pressure):
    totals = []
    if len(open_valves)>0:
        added_pressure = sum([info[valve]['rate'] for valve in open_valves]) 
    else: 
        added_pressure = 0
    # Open valve if not opened
    if at_valve not in open_valves or info[at_valve]['rate']!=0:
        next_open_valves = deepcopy(open_valves)
        next_open_valves.append(at_valve)
        total = best_path(at_valve,next_open_valves,minutes+1,pressure+added_pressure)
        totals.append(total)
    # Move to another valve 
    for next_valve in info[at_valve]['paths']:
        if next_valve not in open_valves:
            total = best_path(next_valve, deepcopy(open_valves), minutes+1, pressure+added_pressure)
            totals.append(total)
    
    if len(totals)>0:
        return max(totals)
    while minutes < 30:
        added_pressure = sum([info[valve]['rate'] for valve in open_valves])
        pressure += added_pressure
        minutes += 1


    return pressure


print(best_path('AA',[],0,0))
