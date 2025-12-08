s = input()

print(s[0] + s[1])

print(s[0:2])

res = ''
for i in range(0, 2):  # 0, 1
    res += s[i]
print(res)
