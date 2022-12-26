import sys
import math
import json

def jprint(obj):
    print(json.dumps(obj, indent=2))

def lprint(lst):
    print(*lst, sep='\n')

file = sys.argv[1] if len(sys.argv)>1 else '0.in'
lines = open(file).readlines()
for line in lines:
    line = line.strip() 
lprint(lines)
