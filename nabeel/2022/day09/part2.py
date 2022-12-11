from math import ceil
from time import sleep

import numpy as np
import cv2

inputfile = open('test2.txt', 'r')
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
print(f'size: {width},{height}')
start = [mapLimits['D'],mapLimits['L']]
chain = [[mapLimits['D'],mapLimits['L']]for _ in range(10)]
print(f'start: {start}')
fps = 25
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (height, width), False)

def buildGrid():
    # print(f'grid: {height}x{width}')
    row = width*" "
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

    def showChain(link,i):
        i = str(i-1)
        show(link, i)
    [showChain(link, len(chain)-i) for i,link in enumerate(chain[::-1])]
    # print(*grid[::-1],sep='\n')

    return grid

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

def makeNP(grid):
    rows = len(grid)
    cols = len(grid[0])
    size = [rows, cols]
    data = np.zeros(size, dtype=np.uint8)

    def addPoint(row, col, char):
        out_char = 0
        if char == '#':
            out_char = 125
        if char in '0123456789':
            out_char = 256
        data[row][col] = out_char

    for row in range(rows): 
        for col in range(cols):
            addPoint(row, col, grid[row][col]) 

    # data =np.uint8(data)
    return data


tail_history = []
for linenum, line in enumerate(lines):
    print(f'{linenum}/{len(lines)}')
    # print(line)
    idx, pn = moveGrid[line[0]]
    for _ in range(int(line[1])):
        # print(*chain,sep='\n')
        chain[0][idx] += pn
        for i in range(1,len(chain)):
            chain[i] = moveTail(chain[i-1], chain[i])

        # print('===========')
        # print(*chain,sep='\n')
        tail_history.append(chain[-1])
        grid = showGrid(tail_history)
        data = makeNP(grid[::-1])
        # print(data[11:14])
        out.write(data)
        cv2.imwrite(f'pics/image_{linenum}_{_}.jpg', data)
        # cv2.imshow('image', data)
        cv2.waitKey(0)
        # a = input()
        # sleep(0.25)

print(len(set([str(i) for i in tail_history])))

out.release()
