"""
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
"""

prime_number_list = []
least_common_multiple = 1
for number in range(2, 21):
    for prime_number in prime_number_list:
        if number % prime_number == 0:
            break
    else:
        prime_number_list.append(number)
        power_number = number
        while True:
            if power_number * number > 20:
                break
            power_number *= number
        least_common_multiple *= power_number
print(least_common_multiple)