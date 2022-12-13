import math

file = 'in0'
# file = 'in1'
lines = open(file).readlines()
hills = [line.strip() for line in lines]
print(*hills, sep='\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rank(char):
    if char == 'S': return alphabet.index('a')
    if char == 'E': return alphabet.index('z')
    return alphabet.index(char)

def canStep(hereRank:int, there:str):
    if rank(there) <= hereRank+1:
        return True
    return False

h_edges = (-1,len(hills))
v_edges = (-1, len(hills[0]))
def in_bounds(coord):
    row,col = coord
    return row not in h_edges and col not in v_edges

def checkPath(coord, path:list):
    row,col = coord
    here = hills[row][col]
    path.append(coord)
    if here == 'E': return len(path)
    next_steps = [n for n in checkNeighbours(here, coord, path) if n is not None]
    print(f'{coord}->{hills[coord[0]][coord[1]]}->{[hills[step[0]][step[1]] for step in next_steps]}')
    if len(next_steps) == 0: return math.inf
    return min([checkPath(step, path) for step in next_steps])

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
    return validNeighbours

print(checkPath((0,0),[]))
# print(checkPath((20,0),[]))
