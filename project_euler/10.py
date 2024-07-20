"""
10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

이백만(2,000,000) 이하 소수의 합은 얼마입니까?
"""

number_list = list(range(0, 2000000))
is_prime_number = [True] * 2000001
is_prime_number[0], is_prime_number[1] = False, False

for prime_num in range(2, int(pow(2000000, 0.5))):
    n = 2
    while prime_num * n <= 2000000:
        is_prime_number[prime_num * n] = False
        n += 1
print(sum(filter(lambda x: is_prime_number[x] == True, range(2000001))))
