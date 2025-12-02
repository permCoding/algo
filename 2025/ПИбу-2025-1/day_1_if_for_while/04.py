def get_S(side_1, side_2):
    s = side_1 * side_2
    return s


# диалог пользователя с программой
a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

print(f"Площадь прямоугольника - {get_S(a, b)}")


