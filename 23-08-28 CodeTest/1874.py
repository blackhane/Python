from collections import deque

num = int(input())
arr = []

for i in range(1,num+1):
    arr.append(i)
q = deque(arr)

while len(q) > 1:
    q.popleft()
    q.rotate(-1)

print(q[0])