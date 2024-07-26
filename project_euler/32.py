"""
1부터 n까지의 각 숫자를 한 번씩만 써서 만들 수 있는 수를 팬디지털(pandigital)이라고 합니다.
예를 들면 15234는 1부터 5의 숫자가 한 번씩만 쓰였으므로 1 ~ 5 팬디지털입니다.

7254라는 수는 그런 면에서 특이한데, 39 × 186 = 7254 라는 곱셈식을 만들 때 이것이 1 ~ 9 팬디지털이 되기 때문입니다.

이런 식으로 a × b = c 가 1 ~ 9 팬디지털이 되는 모든 c의 합은 얼마입니까?

(참고: 어떤 c는 두 개 이상의 (a, b)쌍에 대응될 수도 있는데, 이런 경우는 하나로 칩니다)
"""


def solve_pandigital(num: str):
    global is_used, number_set
    if len(num) == 9:
        if int(num[0]) * int(num[1:5]) == int(num[5:]) or int(num[:2]) * int(num[2:5]) == int(num[5:]):
            number_set.add(int(num[5:]))
    for n in range(1, 10):
        if is_used[n]:
            continue    
        else:
            is_used[n] = True
            solve_pandigital(num + str(n))
            is_used[n] = False

is_used = [False for _ in range(10)]
number_set = set()
solve_pandigital("")
print(sum(number_set))