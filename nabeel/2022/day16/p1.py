import sys
import math
import json

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
# lprint(lines)

valves = []
rate = {}
paths = {}

for line in lines:
    VT = line.split(';')
    V = VT[0].split()
    valves.append(V[1]) 
    valve = V[1]
    paths[valve] = [tunnel.strip(',') for tunnel in VT[1].split()[4:]]
    rate[valve] = int(V[-1].split('=')[-1])

# Initial numbers 
tunnels = [[math.inf]*len(valves) for _ in valves]
for idx1,fromValve in enumerate(valves):
    for toValve in paths[fromValve]:
        tunnels[idx1][valves.index(toValve)] = 1

# lprint(tunnels)

for _ in range(len(valves)):
    for fromValve in valves:
        for toValve in valves:
            if fromValve != toValve and tunnels[valves.index(fromValve)][valves.index(toValve)]!=math.inf:
                # print(fromValve,toValve)
                for idx in range(len(valves)):
                    # print(idx)
                    includeValve = idx!=valves.index(fromValve) and idx!=valves.index(toValve)
                    if includeValve and tunnels[valves.index(toValve)][idx]!=math.inf:
                        # print('\t',toValve,valves[idx])
                        old = tunnels[valves.index(fromValve)][idx]
                        new = tunnels[valves.index(fromValve)][valves.index(toValve)] + tunnels[valves.index(toValve)][idx]
                        if new<old:
                            tunnels[valves.index(fromValve)][idx] = new

for idx1, fromValve in enumerate(valves):
    for idx2,toValve in enumerate(valves):
        if rate[toValve]<=0:
            tunnels[idx1][idx2] = math.inf

lprint(list(zip(valves,tunnels)))
jprint(rate)

all_open = len([val for key,val in rate.items() if val >0])
print(all_open)
# jprint(paths)

tunnel_paths = {}
for valve,tunnel_list in zip(valves,tunnels):
    tunnel_paths[valve] = {}
    for t_valve, t_time in zip(valves,tunnel_list):
        if t_time != math.inf:
            tunnel_paths[valve][t_valve] = t_time

jprint(tunnel_paths)

from collections import deque
from copy import deepcopy
memo = {}
Q = deque()
max_pressure = 0
Q.append(('AA',0,[],0,0,''))
i = 0
while len(Q):
    i += 1
    if i%100_000 == 0:
        i = 0
        print(f'current max: {max_pressure}')
        # input()
    state = Q.pop()
    # input()
    valve = state[0]
    minutes = state[1]
    opened_valves = deepcopy(state[2])
    opened_rate = state[3]
    pressure_before = state[4]
    logs = state[5]
    if minutes >30 or str((valve,opened_valves,minutes)) in memo.keys():
        continue
    print(max_pressure, state[:-1])
    memo[str((valve,opened_valves,minutes))]=minutes
    if minutes == 30 and pressure_before>max_pressure:
        max_pressure = pressure_before
        print(f'New max {max_pressure} {50*"*"}')
        print(logs)
        # input()
        continue
    for toValve, duration in tunnel_paths[valve].items():
        if rate[toValve]!=0 and toValve not in opened_valves:
            # go to valve, takes n minutes so add opened rate to initial pressure n times
            # n = tunnels[valves.index(valve)][valves.index(toValve)]
            # print(f'from {valve} to {toValve} in {duration} minutes')
            pressure_after = pressure_before + duration*opened_rate
            newlogs = logs + f'@{minutes} take {duration} mins to go to {toValve} rate:{opened_rate} pressure:{pressure_after}\n'
            new_minutes = minutes+duration
            if new_minutes<=30:
                Q.append((toValve, new_minutes, opened_valves, opened_rate, pressure_after,newlogs))
    if minutes<30 and (len(opened_valves)>=30/4 or len(opened_valves)==all_open):
        pressure_after = pressure_before+opened_rate
        newlogs = logs + f'@{minutes} Running all @{valve} rate: {opened_rate} pressure:{pressure_after}\n'
        new_minutes = minutes+1
        if new_minutes<=30:
            Q.append((valve, new_minutes, opened_valves, opened_rate, pressure_after,newlogs))
        # print(opened_valves, newlogs)
    if valve not in opened_valves and rate[valve]!=0:
        # open valve, takes 1 minute, pressure rate is constant, total pressure increase by opened rate before adding new pressure
        # print(f'open valve {valve}')
        opened_valves.append(valve)
        pressure_after = pressure_before+opened_rate
        opened_rate += rate[valve]
        # print(f'opened rate changed to {opened_rate}')
        newlogs = logs + f'@{minutes} take 1 min to open {valve}\n'
        Q.append((valve, minutes+1, opened_valves, opened_rate, pressure_after,newlogs))

    del valve
    del minutes
    del opened_valves
    del opened_rate
    del pressure_before
    del logs

print(max_pressure)
