import math

file = 'in0'
lines = open(file).readlines()
hills = [line.strip() for line in lines]
print(*hills, sep='\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rank(char):
    if char == 'S': return alphabet.index('a')
    if char == 'E': return alphabet.index('z')
    return alphabet.index(char)

def canStep(hereRank:int, there:str):
    return rank(there) <= hereRank+1

row_max = len(hills)
col_max = len(hills[0])

def in_bounds(coord):
    row,col = coord
    return 0<=row<row_max and 0<=col<col_max

def checkNeighbours(here, coord, path:list):
    row, col = coord
    hereRank = rank(here)
    neighbours = [(0,1),(1,0),(0,-1),(-1,0)]
    def fn(coord, neighbour):
        row,col = coord
        nrow,ncol = neighbour
        candidate = (row+nrow,col+ncol)
        if in_bounds(candidate)  and candidate not in path:
            there = hills[row+nrow][col+ncol]
            if canStep(hereRank, there):
                return candidate
            # print(f'inbounds but cannot step to {there}')
        # print(f'{candidate} is out of bounds')

    validNeighbours = [fn(coord, neighbour) for neighbour in neighbours]
    # print(f'@ {here} can go to {validNeighbours}')
    validNeighbours = [neighbour for neighbour in validNeighbours if neighbour is not None]
    return validNeighbours

def findStart():
    for row in range(row_max):
        for col in range(col_max):
            if hills[row][col] == 'S':
                return (row,col)

path = set()
checkQ = [(findStart(),0)]
here = 'S'
while len(checkQ)>0:
    coord, dis = checkQ[0]
    checkQ.remove(checkQ[0])
    if coord in path:
        continue
    path.add(coord)
    row,col = coord
    here = hills[row][col]
    # print(here)
    if here == 'E':  
        print(dis, 'done')
        break
    next_steps = checkNeighbours(here, coord, path) 
    _ = [checkQ.append((next_step,dis+1)) for next_step in next_steps]

def nice(step):
    r,c = step
    return hills[r][c]
print(*[nice(step) for step in path],sep='->')
# print(list(path)[:dis])

# grid = [[' ' for _ in range(col_max)] for _ in range(row_max)]
# print(*grid, sep='\n')
# for step in (path):
#     r,c = step
#     grid[r][c] = '*'
# print(*grid, sep='\n')
