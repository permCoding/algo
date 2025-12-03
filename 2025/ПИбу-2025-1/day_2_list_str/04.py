lst = [1, 2, 45, 12, 99]

sm, i = 0, 0
while i < len(lst):
    if lst[i] % 2 != 0:  # нечётное
        sm += lst[i]
    i += 1
print(sm)
