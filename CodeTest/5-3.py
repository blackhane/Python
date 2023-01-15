"""
2023-01-12
박진휘
코딩테스트 5-3
"""
def hansu(a):
    sum = 0
    for i in range(1, a+1):
        num = list(map(int, str(i)))
        if i <= 99:
            sum += 1
        else:
            if num[0]-num[1] == num[1] - num[2]:
                sum += 1
    return sum

x = int(input())
print(hansu(x))