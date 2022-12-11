from math import ceil
from time import sleep
inputfile = open('test.txt', 'r')
inputfile= open('input.txt', 'r')
lines = inputfile .readlines()
lines = [line.strip().split() for line in lines]
# print(*lines, sep='\n')
mapLimits = {
    'R':0,
    'U':0,
    'L':0,
    'D':0
}
for line in lines:
    direction = line[0]
    steps = line[1]
    mapLimits[direction] = mapLimits[direction] + int(steps)

# [print(key, mapLimits[key]) for key in mapLimits.keys()]

width = mapLimits['R']+mapLimits['L']
height = mapLimits['U']+mapLimits['D']
start = [mapLimits['D'],mapLimits['L']]
head = start
tail = start
print(f'start: {start}')

def buildGrid():
    # print(f'grid: {height}x{width}')
    row = width*"*"
    grid = [row for _ in range(height)]
    # print(*grid[::-1],sep='\n')
    return grid

    
def showGrid(history):
    grid = buildGrid()

    def show(pos,mark): 
        temp = list(grid[pos[0]-1]) 
        temp[pos[1]-1] = mark
        grid[pos[0]-1] = "".join(temp)
    
    show(start,'S')
    for log in history:
        show(log, '#')
    show(tail,'T')
    show(head,'H')
    print(*grid[::-1],sep='\n')

moveGrid = {
    'R':(1,1),
    'L':(1,-1),
    'U':(0,1),
    'D':(0,-1)
}

def add(a,b):
    return [a[0]+b[0], a[1]+b[1]]

def dif(a,b):
    return [a[0]-b[0], a[1]-b[1]]

def pos(a):
    return [abs(val) for val in a]

def div(a,val):
    return [ceil(a[0]/val), ceil(a[1]/val)]
    
def replace(a,b,idx):
    a[idx] = b[idx]
    return a

def moveTail(head,tail):
    body = dif(head,tail)
    # print(body)
    absbody = pos(body)
    # print(absbody)
    stretch = 2 in absbody
    # print(stretch)
    if not stretch:
        change = [0,0]
    else:
        change = div(body,2)
        # print(change)
        if 1 in absbody:
            idx = absbody.index(1)
            # print(idx)
            change = replace(change, body, idx)
            # print(change)

    tail = add(tail, change)
    return tail

tail_history = []
for line in lines:
    # print(line)
    idx, pn = moveGrid[line[0]]
    for _ in range(int(line[1])):
        head[idx] += pn
        # print(head)
        tail = moveTail(head,tail)
        tail_history.append(tail)
        # showGrid(tail_history)
        # a = input()
        # sleep(0.25)

print(len(set([str(i) for i in tail_history])))
