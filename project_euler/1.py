"""
10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.

1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
"""

# first
def three_or_five(number: int) -> int:
    if number % 3 == 0 or number % 5 == 0:
        return number
    return 0

sum_number = sum(map(three_or_five, range(1, 1000)))
print(sum_number)


# second
def get_arithmetic_series(number: int, common_difference: int):
    if number < common_difference:
        return 0
    nst_number = number - number % common_difference
    n = number // common_difference
    arithmetic_series = n * (common_difference + nst_number) // 2
    return arithmetic_series

sum_number = get_arithmetic_series(1000, 3) + get_arithmetic_series(1000, 5) - get_arithmetic_series(1000, 15)
print(sum_number)