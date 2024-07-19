"""
어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

600851475143의 소인수 중에서 가장 큰 수를 구하세요.
"""


number = 600851475143
start_number = 2
while number > start_number:
    if number % start_number == 0:
        number //= start_number
        continue
    start_number += 1
last_prime_number = start_number
print(last_prime_number)