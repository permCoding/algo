s = '12340567'
s = "12340 weugviuwegv fweuj567"

print(s[0])
print(s[1])

print(s[-1])
print(s[-2])
print(s[-3])

for i in range(len(s)):
    print(i, s[i])



# def get_sum_digits(n):
#     sm = 0
#     while n > 0:
#         sm += n % 10  # sm = sm + n % 10
#         n //= 10  # n = n // 10
#     return sm


# print(get_sum_digits(127))  # 10
# print(get_sum_digits(1))    # 1
# print(get_sum_digits(90009))  # 18

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