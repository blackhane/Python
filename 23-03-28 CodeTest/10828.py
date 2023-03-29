import sys

n = int(input())

arr = []
for i in range(n):
    cm = list(sys.stdin.readline().split())
    if(cm[0] == "push"):
        arr.append(cm[1])
    elif(cm[0] == "pop"):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[-1])
            del arr[-1]
    elif(cm[0] == "size"):
        print(len(arr))
    elif(cm[0] == "empty"):
        if(len(arr)):
            print(0)
        else:
            print(1)
    elif(cm[0] == "top"):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[-1])