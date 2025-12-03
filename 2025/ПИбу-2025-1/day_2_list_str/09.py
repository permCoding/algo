lst = [1, 2, 15, 12, 9, 16]

sm_even = sum(elm for elm in lst if elm % 2 == 0)
sm_odd  = sum(elm for elm in lst if elm % 2 != 0)
print(sm_odd if sm_odd > sm_even else sm_even)

"""
вычислить сумму четных и нечетных элементов списка
вывести на экран только бо`льшую сумму
"""