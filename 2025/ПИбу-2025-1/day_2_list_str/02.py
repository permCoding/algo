lst = [12, '33', 12.45, 12 != 0]

for i in 0,1,2,3:
    print(i, lst[i])

for i in range(0, len(lst), 1):
    print(i, lst[i])

for i in range(len(lst)):
    print(i, lst[i])

for i in range(4):
    print(i, lst[i])
