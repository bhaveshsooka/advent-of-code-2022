import sys
import math

file = sys.argv[1] if len(sys.argv)>1 else '0.in'
lines = open(file).readlines()
lines = [line.strip() for line in lines]
print(*lines, sep='\n')
