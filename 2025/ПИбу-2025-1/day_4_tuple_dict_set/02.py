line_R = "I V X L C D M"
line_D = "1 5 10 50 100 500 1000"

number_Roman = "LXXIV"  # 50 + 10 + 10 + 1 + 5 = 71

lst_R = line_R.split(" ")
lst_D = [int(elm) for elm in line_D.split(" ")]  # ['1', '5', '10', '50', '100', '500', '1000']


print(lst_R)
print(lst_D)

pos = lst_R.index("X")
print(lst_D[pos])



"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
"""