"""
오일러는 다음과 같은 멋진 이차식을 제시했습니다.

n2 + n + 41
이 식의 n에다 0부터 39 사이의 수를 넣으면, 그 결과는 모두 소수가 됩니다.
하지만 n = 40일 때의 값 402 + 40 + 41 은 40×(40 + 1) + 41 이므로 41로 나누어지고, n = 41일 때 역시 412 + 41 + 41 이므로 소수가 아닙니다.

컴퓨터의 발전에 힘입어 n2 − 79n + 1601 이라는 엄청난 이차식이 발견되었는데, 이것은 n이 0에서 79 사이일 때 모두 80개의 소수를 만들어냅니다. 이 식의 계수의 곱은 -79 × 1601 = -126479가 됩니다.

아래와 같은 모양의 이차식이 있다고 가정했을 때,

n2 + an + b   (단 | a | < 1000, | b | < 1000)
0부터 시작하는 연속된 n에 대해 가장 많은 소수를 만들어내는 이차식을 찾아서, 그 계수 a와 b의 곱을 구하세요.
"""

number_list = list(range(0, 10001))
is_prime_number = [True] * 10001
is_prime_number[0], is_prime_number[1] = False, False
max_n, max_a, max_b = 0, 0, 0

for prime_num in range(2, int(pow(10000, 0.5))):
    n = 2
    while prime_num * n <= 10000:
        is_prime_number[prime_num * n] = False
        n += 1

prime_number_list = list(filter(lambda x: is_prime_number[x] == True, range(2, 10001)))
for prime_num in prime_number_list:
    if prime_num >= 1000:
        break
    for a in range(prime_num * -1 + 1, 1001):
        n = 0
        while True:
            if n ** 2 + a * n + prime_num in prime_number_list:
                n += 1
            else:
                if n > max_n:
                    max_n, max_a, max_b = n, a, prime_num
                break

print(max_a * max_b)