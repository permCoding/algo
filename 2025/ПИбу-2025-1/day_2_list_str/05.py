lst = [1, 2, 45, 12, 99]

sm = 0
for i in range(len(lst)):
    if lst[i] % 2 != 0:  # нечётное
        sm += lst[i]
print(sm)
