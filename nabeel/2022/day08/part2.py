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

def score(erow, ecol, direction):
    tree = eval[erow][ecol]
    direction_score = 0
    for other in direction:
        direction_score +=1
        if tree <= other: 
            break
    return direction_score

max_score = 0
for erow in range(e_height):
    for ecol in range(e_width):
        news = getNEWS(erow, ecol, height, width)
        tree_score = 1
        print(eval[erow][ecol])
        for direction in news:
            direction_score = score(erow, ecol, direction) 
            print(f'\t{direction} ->{direction_score}')
            tree_score *= direction_score
        print(tree_score)
        if tree_score > max_score:
            max_score = tree_score

print(max_score)
