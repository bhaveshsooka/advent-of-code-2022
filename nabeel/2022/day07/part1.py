from drive import Drive

input = open('test.txt', 'r')
# input = open('input.txt', 'r')
lines = input.readlines()
# output = open('output.txt', 'w')
lines = [line.strip() for line in lines]
# print(*lines, sep='\n')
# [print(idx, line) for idx,line in enumerate(lines)]

commands = [idx for idx,line in enumerate(lines) if '$' in line]
commands.append(len(lines))
# print(commands)

drive = Drive()

for idx in range(len(commands)-1):
    command = lines[commands[idx]:commands[idx+1]]
    print(command)
    drive.cmd(command)

drive.pwd()

directory = drive.drive
sizes = {}

def item_size(directory, file):
    if type(directory[file]) == int:
        return directory[file]
    elif type(directory[file]) == dict:
        size = sum([item_size(directory[file], _file) for _file in directory[file]])
        print(file, size)
        sizes[file] = size
        return size

size = item_size(directory,'/')

print(sizes)

filter = [sizes[directory] for directory in sizes if sizes[directory]<=100000]
print(*filter)

solution = sum(filter)
print('solution ',solution)
