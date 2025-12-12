from random import randint

numbers = []
for i in range(100):
    numbers += [randint(100, 999)]
print(numbers)

st = set()
for elm in numbers: st.add(elm)

print(sorted(st), len(st))
