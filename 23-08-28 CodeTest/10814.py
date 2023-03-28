import sys

n = int(input())

arr = []
for i in range(n):
    name = sys.stdin.readline().split()
    arr.append(name)
arr.sort(key=lambda x:int(x[0]))

for i in range(len(arr)):
    print(arr[i][0] + " " + arr[i][1])