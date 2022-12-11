input = open('test.txt', 'r')
input = open('input.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]
print(*lines, sep='\n')
height = len(lines)
width = len(lines[0])
print(f'height: {height}')
print(f'width: {width}')

eval = [[] for _ in range(height-2)]
for row in range(1,height-1):
    for col in range(1, width-1):
        eval[row-1].append(lines[row][col])
print(*eval, sep='\n')
e_height = len(eval)
e_width = len(eval[0])
print(f'height: {e_height}')
print(f'width: {e_width}')

def getNEWS(erow, ecol, height, width):
    row = erow+1
    col = ecol+1
    north = [lines[idx][col] for idx in range(row-1,-1,-1)]
    east = [lines[row][idx] for idx in range(col-1,-1,-1)]
    south = [lines[idx][col] for idx in range(row+1,height,1)]
    west = [lines[row][idx] for idx in range(col+1,width,1)]
    # print(f'{row} {col}: {west}')
    return [north, east, south, west]

def is_visible(erow, ecol, direction):
    tree = eval[erow][ecol]
    for other in direction:
        if tree <= other: return False
    return True

interior_visible_counter = 0
for erow in range(e_height):
    for ecol in range(e_width):
        news = getNEWS(erow, ecol, height, width)
        for direction in news:
            if is_visible(erow, ecol, direction):
                interior_visible_counter +=1
                break
print(interior_visible_counter)

exterior_visible = 2*height + 2*width - 4

total_visible = interior_visible_counter + exterior_visible
print(total_visible)
