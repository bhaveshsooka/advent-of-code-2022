input = open('test.txt', 'r')
# input = open('input.txt', 'r')
lines = input.readlines()
lines = [line.strip() for line in lines]

import json
class DirectoryObject:
    def __init__(self, path:str, info:str) -> None:
        self.path = path
        if 'dir' in info:
            self.type = info
            self.mem = 0
            self.children = []
            return
        self.type = 'file'
        self.mem = int(info)

    def addChild(self,path:str):
        self.children.append(path)

    def size(self):
        if self.type == 'file': return self.mem
        self.mem = sum([directoryObjects[child].size() for child in self.children])
        return self.mem

directoryObjects = {
    '/': DirectoryObject('/','dir')
}

cwd = []

def pwd(object:str='',show=False):
    pwd = '/'.join(cwd)+'/'+object
    if '//' in pwd:
        pwd = pwd[1:]
    if show: print(pwd)
    return pwd

def command(line:str):
    if '$ ls' in line: return
    if '$ cd ..' in line:
        cwd.pop()
        return
    # $ cd <directory>
    nextDir = line.split()[2]
    cwd.append(nextDir)
    print(f'cwd: {pwd()}')
    
def addObject(line:str):
    [info,newObject] = line.split()
    newObject = pwd(newObject)+'/'
    print(newObject)
    directoryObjects.update({
        newObject:DirectoryObject(newObject, info)
    })
    directoryObjects[pwd()].addChild(newObject)

for line in lines:
    print(line)
    if '$' in line:
        command(line)
    else:
        addObject(line)


print(directoryObjects['/'].size())

vals = [do.__dict__['mem'] for do in directoryObjects.values() if do.__dict__['type']== 'dir' and do.__dict__['mem']<=100_000]
# print(vals)

sum_of_dir_lte_100_000 = sum(vals)
print(f'sum of dirs <= 100,000: {sum_of_dir_lte_100_000:,}')

current_disk = directoryObjects['/'].size()
print(f'current_disk: {current_disk:,}')

max_disk = 70_000_000
update_threshold = 30_000_000
min_disk_level = max_disk-update_threshold
print(f'min level:{min_disk_level:,}')

removed_dir = min([do.__dict__['mem'] for do in directoryObjects.values() if current_disk-do.__dict__['mem']<min_disk_level])
print(removed_dir)
