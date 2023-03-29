n, m = map(int,input().split())
arr = list(map(int,input().split()))

result = []
for i in range(len(arr)-2):
    for j in range (i+1, len(arr)-1):        
        for k in range (j+1, len(arr)):
             if(arr[i]+arr[j]+arr[k] > m):
                 continue
             else:
                result.append(arr[i]+arr[j]+arr[k])

print(max(result))
