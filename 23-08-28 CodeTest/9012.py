n = int(input())

for i in range(n):
    vps = list(input())
    r = 0
    for i in range(len(vps)):
        if(vps[i] == "(" and r >= 0):
            r += 1
        elif(vps[i] == ")" and r > 0):
            r -= 1
        elif(vps[i] == ")" and r == 0):
            r = -1
            break
    if(r == 0):
        print("YES")
    else:
        print("NO")