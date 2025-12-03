def get_sum_digits(n):
    return sum(int(elm) for elm in str(n))


print(get_sum_digits(127))  # 10
print(get_sum_digits(1))    # 1
print(get_sum_digits(90009))  # 18

"""
написать функцию, которая будет принимать целое число 
и возвращать сумму цифр
127 % 10 => 7
 12 % 10 => 2
  1 % 10 => 1
       0 => stop

print(17 / 5)  # 3.4
print(17 // 5)  # 3
"""