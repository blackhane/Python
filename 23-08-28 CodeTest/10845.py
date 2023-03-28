import sys

n = int(input())

arr = []

for i in range(n):
    com = list(sys.stdin.readline().split())

    if(com[0] == "push"):
        arr.append(com[1])
    elif(com[0] == "pop"):
        if arr:
            print(arr[0])
            del arr[0]
        else:
            print(-1)
    elif(com[0] == "size"):
        print(len(arr))
    elif(com[0] == "empty"):
        if(len(arr) == 0):
            print(1)
        else:
            print(0)
    elif(com[0] == "front"):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[0])
    elif(com[0] == "back"):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[-1])

