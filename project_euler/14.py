"""
양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.

n → n / 2 (n이 짝수일 때)
n → 3 n + 1 (n이 홀수일 때)

13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도 마지막에는 1로 끝나리라 생각됩니다.
(역주: 이것은 콜라츠 추측 Collatz Conjecture이라고 하며, 이런 수들을 우박수 hailstone sequence라 부르기도 합니다)

그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데 가장 긴 과정을 거치는 수는 얼마입니까?

참고: 계산 과정에는 백만을 넘어가는 수가 나와도 괜찮습니다.
"""



least_count_list = [0 for _ in range(1000001)]

multiple = 2
count_of_multiple = 1
while multiple <= 1000000:
    least_count_list[multiple] = count_of_multiple
    multiple *= 2
    count_of_multiple += 1

number = 2
while number <= 1000000:
    new_number = number
    count_of_collatz = 0
    while True:
        if new_number <= 1000000 and least_count_list[new_number]:
            least_count_list[number] = count_of_collatz + least_count_list[new_number]
            number += 1
            break
        else:
            if new_number % 2:
                new_number = new_number * 3 + 1
            else:
                new_number //= 2
            count_of_collatz += 1
print(least_count_list.index(max(least_count_list)))

