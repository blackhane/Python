a,b,c = map(int, input().split())
rs1 = (a+b) % c
rs2 = ((a % c)+(b % c)) % c
rs3 = (a * b) % c
rs4 = ((a % c) * (b % c)) % c
print(rs1)
print(rs2)
print(rs3)
print(rs4)