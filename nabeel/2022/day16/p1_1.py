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
# lprint(lines)

valves = []
rates = []
toValves = []

for line in lines:
    VT = line.split(';')
    V = VT[0].split()
    valves.append(V[1]) 
    rates.append(int(V[-1].split('=')[-1]))
    toValves.append([tunnel.strip(',') for tunnel in VT[1].split()[4:]]) 

# print(valves)
# print(rates)
# print(toValves)
print(list(zip(valves,rates)))

# Initial numbers 
tunnels = [[math.inf]*len(valves) for _ in valves]
for idx,fromValve in enumerate(valves):
    # print('From: ',fromValve)
    for toValve in toValves[idx]:
        # print('To: ',toValve)
        tunnels[valves.index(fromValve)][valves.index(toValve)] = 1

lprint(tunnels)
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
    # lprint(tunnels)
    # input()

# lprint(tunnels)

def merge(tunnels,rates,minute):
    assert len(tunnels)==len(rates)
    l = len(rates)
    
    display = [[math.inf]*l for _ in range(l)]
    for fromIdx in range(l):
        for toIdx in range(l):
            if fromIdx!=toIdx:
                display[fromIdx][toIdx] = (minute-tunnels[fromIdx][toIdx]-1)*rates[toIdx]
    
    return display

CD = 30
currentValve = valves[0]
valveTime = []
# for minute in range(CD,0-1,-1):
minute = CD
print(f'Minute {CD-minute}')
input()
while ((minute>=0) and (sum(rates) >0)):
    display = merge(tunnels,rates,minute)
    # print(rates)
    # lprint(display)
    print(display[valves.index(currentValve)])
    tops = [val if val !=math.inf else 0 for val in display[valves.index(currentValve)]]
    print('tops',tops)
    checkTops = deepcopy(tops)
    checkTops.sort(reverse=True)
    print('check tops',checkTops)
    maxSumTop = 0
    top = 0
    for checkTop in checkTops[:3]:
        checkValve = valves[tops.index(checkTop)]
        print(f'Checking Top: {checkTop} for valvle {checkValve}')
        thisValve = deepcopy(checkValve)
        checkVT = deepcopy(valveTime)
        checkRates = deepcopy(rates)
        checkminute = deepcopy(minute)
        for i in range(5):
            checkDisplay = merge(tunnels,checkRates,checkminute)
            # print(checkValve, currentValve)
            # print(checkDisplay[valves.index(checkValve)])
            thisTop = max([val for val in checkDisplay[valves.index(thisValve)] if val != math.inf])
            checkValveIdx = checkDisplay[valves.index(thisValve)].index(thisTop)
            checkminute = checkminute-tunnels[valves.index(thisValve)][checkValveIdx]-1 
            checkValve = valves[checkValveIdx]
            checkVT.append((thisValve, rates[checkValveIdx], minute, thisTop))
            checkRates[checkValveIdx] = 0
        total = sum([VT[3] for VT in checkVT])
        print(checkValve, checkTop,checkVT, total)
        if total > maxSumTop:
            maxSumTop = total
            top = checkTop
    print(f'Selected top {top} for {valves[tops.index(top)]}')


    bestValveIdx = display[valves.index(currentValve)].index(top)
    # bestValveIdx = valves.index(input('best valve idx: '))
    # top = display[valves.index(currentValve)][bestValveIdx]

    minute = minute-tunnels[valves.index(currentValve)][bestValveIdx]-1 
    currentValve = valves[bestValveIdx]
    print(f'Minute {CD-minute} open valve {valves[bestValveIdx]}')
    valveTime.append((currentValve, rates[bestValveIdx], minute, top))
    rates[bestValveIdx] = 0
    print(minute)
    print(rates)
    input()

display = merge(tunnels,rates,minute)
lprint(display)
lprint(valveTime)
lprint(tunnels)

total = sum([VT[3] for VT in valveTime])
print(total)
