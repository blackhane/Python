import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda x:(x[0], x[1]))

for i in range(len(arr)):
    print(str(arr[i][0])+" "+str(arr[i][1]))