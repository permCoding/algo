# bin()
# oct()
# hex()
# int()  # 2 .. 36

s = '1001'
print(int(s))  # в десятичную
print(int(s, 10))
print(int(s, 2))  # 9


# 0123456789ABCDEF
print(int('F', 16))  # 15
print(int('10', 16))  # 16
print(int('11', 16))  # 17
print(int('20', 16))  # 32
print(int('2A', 16))  # 42
print(int('32A', 16))  # 42
print(int('H2A', 36))  # 22114
