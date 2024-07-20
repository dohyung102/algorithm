"""
세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
"""

# m(m + n) = 500

for num in range(1, 499):
    if 500 % num:
        continue
    another_num = 500 // num - num
    if another_num <= 0 or num < another_num:
        continue
    first_number, second_number, third_number = pow(num, 2) - pow(another_num, 2), 2 * num * another_num, pow(num, 2) + pow(another_num, 2)
    if pow(first_number, 2) + pow(second_number, 2) == pow(third_number, 2):
        print(first_number * second_number * third_number)