"""
수 145는 신기한 성질이 있습니다. 각 자릿수의 팩토리얼(계승)을 더하면  1! + 4! + 5! = 1 + 24 + 120 = 145 처럼 자기 자신이 됩니다.

이렇게 각 자릿수의 팩토리얼을 더하면 자기 자신이 되는 모든 수의 합을 구하세요.

단, 1! = 1 과 2! = 2 의 경우는 덧셈이 아니므로 제외합니다.
"""

from math import factorial

# first
sum_of_numbers = 0
for num in range(3, 9999999):
    total_value = sum(map(factorial, map(int, str(num))))
    if total_value == num:
        sum_of_numbers += num
print(sum_of_numbers)

# second
sum_of_numbers = sum(filter(lambda x: x == sum(map(factorial, map(int, str(x)))), range(3, 9999999)))
print(sum_of_numbers)