"""
피보나치(Fibonacci) 수열의 각 항은 바로 앞의 항 두 개를 더한 것입니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 됩니까?
"""


# first
fibo = [1, 2]
index = 2
while True:
    next_nunber = fibo[index - 2] + fibo[index - 1]
    if next_nunber >= 4000000:
        break
    fibo.append(next_nunber)
    index += 1

print(sum(fibo[1::3]))



# second
def get_nth_nth_fibonachi_number(n: int):
    nth_fibonachi_number = ((1 + 5**(0.5))**n  - (1 - 5**(0.5))**n) / (2**n * 5**(0.5))
    return int(nth_fibonachi_number)

sum_of_even_number = 0
start_number = 0
while True:
    fibonachi_number = get_nth_nth_fibonachi_number(start_number)
    if fibonachi_number >= 4000000:
        break
    if fibonachi_number % 2 == 0:
        sum_of_even_number += fibonachi_number
    start_number += 1

print(sum_of_even_number)