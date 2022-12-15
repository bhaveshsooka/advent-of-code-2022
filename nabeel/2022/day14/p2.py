import sys
import math
def lprint(lst):
    print(*lst, sep='\n')

file = sys.argv[1] if len(sys.argv)>1 else '0.in'
lines = open(file).readlines()

def fprint(grid,units):
    flatgrid = '\n'.join(grid)
    with open('out','w') as out:
        out.write(str(units)+'\n')
        out.write(flatgrid)



def parse(coords:'list[str]')->'list[tuple]':
    result = []
    for coord in coords:
        lst = coord.split(',')
        lst = [int(item) for item in lst]
        result.append(tuple(lst))
    return result


def parseMap(coords:'list[str]')->'list[tuple]':
    return [tuple(map(int, coord.split(','))) for coord in coords]

lines = [parse(line.strip().split(' -> ')) for line in lines]
# lprint(lines)


def minmax(coords:'list[tuple(int,int)]'):
    x = [coord[0] for coord in coords]
    y = [coord[1] for coord in coords]
    return [ (min(x),min(y)), (max(x),max(y)) ]

minmax_lines = [minmax(line) for line in lines]
grid_range = minmax([i for line in minmax_lines for i in line])
print(grid_range)

def i_range(rc:int):
    return grid_range[1][rc] - grid_range[0][rc] + 1

x_range = i_range(0)
y_range = i_range(1)
grid_min = grid_range[0]

print(f'X range: {x_range}')
print(f'Y range: {y_range}')

space = 1000
shift = 500

grid = [(x_range+space)*'.' for _ in range(grid_min[1]+y_range+2)]
grid[-1] = (x_range+space)*'#' 

# lprint(grid)

def gprint(grid,x,y,sym):
    x = x - grid_min[0] + shift
    grid[y] = grid[y][:x] + sym + grid[y][x+1:]
    return grid

def gprintpoint(grid, point,sym):
    return gprint(grid, point[0],point[1],sym)

for line in lines:
    for point in range(len(line)-1):
        start = line[point]
        end = line[point+1]
        # print(f'{start} -> {end}')
        x_step = 1 if start[0] < end[0] else -1
        for x in range(start[0],end[0]+x_step,x_step):
            # print((x,start[1]))
            grid = gprint(grid, x, start[1],'#')
            
        
        y_step = 1 if start[1] < end[1] else -1
        for y in range(start[1],end[1]+y_step,y_step):
            # print((start[0],y))
            grid = gprint(grid, start[0], y,'#')
grid = gprint(grid, 500,0,'+')
# lprint(grid)

point = (500,0)
def can_move(point,grid)->int: #0,1,2,3,4
    deltas = [(0,1), (-1,1), (1,1)]
    for delta in deltas:
        new = (point[0]+delta[0], point[1]+delta[1])
        # print(f'candidate point {new}')
        if new[1] >= y_range+grid_min[1]+2:
            # print('sand falling into abyss')
            return False
        pos = grid[new[1]][new[0]- grid_min[0]+shift]
        # print(f'item at candidate position: {pos}')
        if pos not in ['#','o']:
            return new
    return point

falling_into_abyss = False
make_sand = True
units = 0
while not falling_into_abyss:
    if make_sand:
        point = (500,0)
        make_sand = False
    # print(f'point start at {point}')
    new_point = can_move(point, grid)
    # print(f'selected candidate point {new_point}')
    if not new_point:
        falling_into_abyss = True
    if new_point==point:
        grid = gprintpoint(grid, point,'o')
        # print(10*"=")
        units += 1
        if units%20_000 == 0:
            fprint(grid,units)
            input()
        if new_point == (500,0):
            break
        make_sand = True

    point = new_point
    # print(f'point end at {point}')
    # input()


# lprint(grid)
fprint(grid,units)
print(units)
