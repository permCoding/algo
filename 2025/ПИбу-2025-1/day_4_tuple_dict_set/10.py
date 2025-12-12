from random import randint

numbers = []
for i in range(20):
    numbers += [randint(0, 9)]
print(numbers)


lst = []
for elm in numbers:
    if elm not in lst:
        lst += [elm]
lst.sort()
print(lst, len(lst))
