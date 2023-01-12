"""
날짜 : 2023-01-11
이름 : 박진휘
내용 : 파이썬 모듈 실습하기
"""
import sub2.calc
import sub2.calc as c
from sub2.calc import *

r1 = sub2.calc.plus(1, 2)
r2 = c.minus(1, 2)
r3 = multi(1, 2)
r4 = div(1, 2)

print(r1)
print(r2)
print(r3)
print(r4)