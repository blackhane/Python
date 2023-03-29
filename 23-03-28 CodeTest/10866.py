import sys
n = int(input())

arr = []
for i in range(n):
    dq = list(sys.stdin.readline().split())
    
    if(dq[0] == "push_front"):
        arr.insert(0, dq[1])
    elif(dq[0] == "push_back"):
        arr.append(dq[1])
    elif(dq[0] == "pop_front"):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[0])
            del arr[0]
    elif(dq[0] == "pop_back"):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[-1])
            del arr[-1]
    elif(dq[0] == "size"):
        print(len(arr))
    elif(dq[0] == "empty"):
        if(len(arr)):
            print(0)
        else:
            print(1)
    elif(dq[0] == "front"):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[0])
    elif(dq[0] == "back"):
        if(len(arr) == 0):
            print(-1)
        else:
            print(arr[-1])