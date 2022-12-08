import json
class Drive:
    def __init__(self):
        self.base = 'drive'
        self.paths = []
        self.cwd = ''
        self.drive = {'/':{}}

    def cd(self, directory:str):
        self.paths.append(directory)
        self.cwd = base+str(*[f"['{path}']" for path in paths])


drive = {'/':{}}
base = 'drive'
paths = []
# ['$ cd /'] 
paths.append('/')
cwd = base+str(*[f"['{path}']" for path in paths])
print(cwd)
# cwd = "drive['/']" 

['$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d']
# create directory as {}/ file as size iff it doesn't exist already
# drive['/']['a'] = {} 
exec(f"{cwd}['a']={{}}")
# drive['/']['b.txt'] = 14848514
exec(f"{cwd}['b.txt']={14848514}")
drive['/']['c.dat'] = 8504156
drive['/']['d'] = {}

print(json.dumps(drive, indent=2))

# ['$ cd a']

# ['$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst']

# ['$ cd e']

# ['$ ls', '584 i']

# ['$ cd ..']

# ['$ cd ..']

# ['$ cd d']

# ['$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']
