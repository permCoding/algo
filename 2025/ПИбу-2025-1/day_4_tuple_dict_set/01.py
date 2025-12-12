lst = list()  # ~ [] - список
tpl = tuple( list("123456") )  # ~ () - кортеж
dct = dict()  # ~ {} - словарь
st = set()  # ~ {} - множество

obj = 1024


lst.append(obj)  # добавление в конец
lst.append(666)  # добавление в конец
lst[-1] = 999  # замена ПОСЛЕДНЕГО элемента
print(lst)

# tpl[-1] = 666  # НЕЛЬЗЯ - замена элемента
print( tpl )
for i in range(len(tpl)): print(tpl[i])

print(st)
st.add(12)
st.add(2222)
st.add(12)
st.add(2222)
st.add(606)
st.add(2222)
print(st)

print(dct)
dct = {
    "пн": 0,
    "вт": 1,
    "ср": 2,
    "чт": 3,
    "пт": 4,
    "сб": 5,
    "вс": 6
}
print(dct)
print(dct.keys())
print(dct.values())
print(dct.items())

keys = list(dct.keys())
print(keys)
# print(dct.keys()[-1])  # так не работает
print(keys[0], keys[-1])
for item in dct.items(): print(item)
for item in dct.items(): print(*item)


"""
ещё бывают: массив, стек, очередь

print(list("123456"))  # ['1', '2', '3', '4', '5', '6']

json

0..7 >7
пн
вт

None
"""