a = input()
b = input()

a = int(a)
b = int(b)

rs1 = b // 100
rs2 = b % 100 // 10
rs3 = b % 100 % 10

print(rs3 * a)
print(rs2 * a)
print(rs1 * a)
print(a * b)