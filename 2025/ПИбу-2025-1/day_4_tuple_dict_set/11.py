from random import randint

numbers = []
for i in range(10):
    numbers += [randint(0, 9)]
print(numbers)


lst = []
for elm in numbers:
    try:
        if elm not in lst:
            lst += [elm]
    except:
        pass

print(sorted(lst), len(lst))
