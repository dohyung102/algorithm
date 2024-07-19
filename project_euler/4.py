"""
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.

두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.

세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
"""

max_palindrome = 0
for first_number in range(999, 100, -1):
    if first_number * 999 < max_palindrome:
        break
    for second_number in range(999, 100, -1):
        number = str(first_number * second_number)
        length = len(number)
        half_length = len(number) // 2
        if number[:half_length] == number[length-1: length - half_length-1: -1]:
            max_palindrome = max(max_palindrome, int(number))
            break
print(max_palindrome)
