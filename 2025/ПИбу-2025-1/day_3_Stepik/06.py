n = 9

print(bin(n)[2:])  # 0b1001
print(oct(n)[2:])  # 0o11
print(hex(n)[2:])  # 0x9

print(hex(219)[2:].upper())  # _____


print(f'{n:b}')
n = 248
print(f"n = {n}; bin(n) = {n:b}")
n = 255
print(f"n = {n}; bin(n) = {n:x}")  # .upper()
h = f"{n:x}".upper()
print(f"n = {n}; hex(n) = {h}")  # .upper()



# int()  # 2 .. 36

