numbers = [2,4,2,3,5,2,7]
elms = [5, 8, 2, 102, 7]

for elm in elms:
    try:
        print(elm, numbers.index(elm))
    except:
        print(f"элемент - {elm} не найден в списке numbers")
