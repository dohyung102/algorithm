"""
n의 약수들 중에서 자신을 제외한 것의 합을 d(n)으로 정의했을 때,
서로 다른 두 정수 a, b에 대하여 d(a) = b 이고 d(b) = a 이면
a, b는 친화쌍이라 하고 a와 b를 각각 친화수(우애수)라고 합니다.

예를 들어 220의 약수는 자신을 제외하면 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 이므로 그 합은 d(220) = 284 입니다.
또 284의 약수는 자신을 제외하면 1, 2, 4, 71, 142 이므로 d(284) = 220 입니다.
따라서 220과 284는 친화쌍이 됩니다.

10000 이하의 친화수들을 모두 찾아서 그 합을 구하세요.
"""

sum_of_divisor_list = [0 for _ in range(10001)]
sum_of_amicable_numbers = 0
for num in range(2, 10001):
    sum_of_divisor = sum({i for i in range(2, int(num ** 0.5) + 1) if num % i == 0 for i in (i, num // i)}) + 1
    if sum_of_divisor <= 10000:
        if sum_of_divisor_list[sum_of_divisor] == num:
            sum_of_amicable_numbers += num + sum_of_divisor
        sum_of_divisor_list[num] = sum_of_divisor
print(sum_of_amicable_numbers)

