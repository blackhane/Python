"""
2023-01-12
박진휘
코딩테스트 5-2
"""
def solve(n):
    n = n + sum(map(int, str(n)))
    return n

noSelfNum = set()

for i in range(1, 10001):
    noSelfNum.add(solve(i))

for j in range(1, 10001):
    if j not in noSelfNum:
        print(j)