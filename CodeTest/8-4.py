import math
import sys
m, n = map(int, sys.stdin.readline().rstrip().split())
ori = [True for i in range(n+1)]
for i in range(2, int(math.sqrt(n)) + 1):
    if ori[i] == True:
        j = 2
        while i * j <= n:
            ori[i*j] = False
            j += 1
for i in range(m, n+1):
    if ori[i]:
        if i != 1:
            print(i)