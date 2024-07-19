"""
소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

이 때 10,001번째의 소수를 구하세요.
"""

prime_number_list = [2]
count_prime_number = 1
while count_prime_number < 10001:
    last_prime_number = prime_number_list[-1]
    square_number = last_prime_number ** 2
    is_prime_number = [True] * (square_number + 1)
    is_prime_number[0], is_prime_number[1] = False, False
    for prime_number in prime_number_list:
        n = 2
        while prime_number * n <= square_number:
            is_prime_number[prime_number * n] = False
            n += 1
    for number in range(last_prime_number + 1, square_number):
        if is_prime_number[number]:
            prime_number_list.append(number)
            count_prime_number += 1
            if count_prime_number == 10001:
                print(number)
                break