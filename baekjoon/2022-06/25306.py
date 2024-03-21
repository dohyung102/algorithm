import sys
sys.stdin = open('25306.txt')

def xor(num1, num2):
    return num1 ^ num2


front_number, end_number = map(int, input().split())
numbers = []
if front_number == end_number:
    answer = front_number
elif end_number - front_number == 1:
    answer = xor(front_number, end_number)
else:
    if front_number % 2:
        numbers.append(front_number)
        front_number += 1
    if not end_number % 2:
        numbers.append(end_number)
        end_number -= 1
    if len(numbers) == 2:
        number1, number2 = numbers
        middle_number = xor(number1, number2)
    elif len(numbers) == 1:
        middle_number = numbers[0]
    else:
        middle_number = 0
    answer = xor(middle_number, ((end_number - front_number + 1) // 2) % 2)
print(answer)
