import json
class Drive:
    def __init__(self):
        self.base = 'self.drive'
        self.paths = []
        self.cwd = ''
        self.drive = {'/':{}}

    def cmd(self, command):
        cmd = command[0]
        print(cmd)
        if '$ cd' in cmd: 
            self.cd(cmd.split(' ')[2])
        elif '$ ls' in cmd: 
            self.ls(command[1:])

    def pwd(self):
        # print(self.cwd)
        print(f"$ cwd {'/'.join(self.paths)[1:]}")
        print(json.dumps(self.drive, indent=2))

    def mkdir(self, directory):
        new_dir = {directory:{}}
        exec(f"{self.cwd}.update({new_dir})")
        print(f"if '{directory}' not in {self.cwd}: {self.cwd}['{directory}']={{}}")
        
    def touch(self, file, size):
        new_file = {file:int(size)}
        exec(f"{self.cwd}.update({new_file})")
        print(f"{self.cwd}['{file}']={size}")

    def cd(self, directory:str):
        if directory == '..':
            self.paths.pop()
        else:
            self.paths.append(directory)
        # print(self.paths)
        self.cwd = self.base+''.join([f"['{path}']" for path in self.paths])
    
    def ls(self, directory:list):
        print(f"$ cwd {'/'.join(self.paths)[1:]}")
        for item in directory:
            [info, name] = item.split(' ')
            if info == 'dir': self.mkdir(name)
            else: self.touch(name, info)


if __name__ == '__main__':

    drive = Drive()

    command = ['$ cd /'] 
    drive.cmd(command)
    drive.pwd()

    command = ['$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d']
    drive.cmd(command)
    drive.pwd()
    # create directory as {}/ file as size iff it doesn't exist already

    command=['$ cd a']
    drive.cmd(command)
    drive.pwd()

    command = ['$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst']
    drive.cmd(command)
    drive.pwd()

    command = ['$ cd ..']
    drive.cmd(command)
    drive.pwd()

    # ['$ cd e']

    # ['$ ls', '584 i']

    # ['$ cd ..']

    # ['$ cd ..']

    # ['$ cd d']

    # ['$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']
