import sys
sys.stdin = open('23845.txt')

length = int(input())
accumulation = [0]*100001
numbers = list(map(int, input().split()))
max_number = 0
for number in numbers:
    accumulation[number] += 1
    if number > max_number:
        max_num = number
answer = 0
while max_number:
    while accumulation[max_number]:
        count = 0
        current_number = max_number
        while accumulation[current_number]:
            accumulation[current_number] -= 1
            current_number -= 1
            count += 1
        answer += max_number * count
    max_number -= 1
print(answer)