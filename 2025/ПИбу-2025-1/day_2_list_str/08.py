lst = [1, 2, 15, 12, 9, 16]

lst_even = [elm for elm in lst if elm % 2 == 0]
lst_odd  = [elm for elm in lst if elm % 2 != 0]
print(lst_even, lst_odd)

# sm_odd, sm_even = 0, 0
# for elm in lst:
#     if elm % 2 != 0:  # нечётное
#         sm_odd += elm
#     else:
#         sm_even += elm

# print(sm_odd if sm_odd > sm_even else sm_even)


"""
вычислить сумму четных и нечетных элементов списка
вывести на экран только бо`льшую сумму
"""