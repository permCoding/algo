line_R = "I V X L C D M"
line_D = "1 5 10 50 100 500 1000"

number_Roman = "IIDIIIM"  # 50 + 10 + 10 + 1 + 5 = 76

tpl_R = tuple(line_R.split(" "))
tpl_D = tuple([int(elm) for elm in line_D.split(" ")])
print(tpl_R)
print(tpl_D)

result = 0
for elm in number_Roman:
    pos = tpl_R.index(elm)
    result += tpl_D[pos]
print(result)


"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
"""