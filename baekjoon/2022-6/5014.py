import sys
sys.stdin = open('5014.txt')

top_floor, initial_floor, target_floor, up, down = map(int, input().split())
building = [-1] * (top_floor + 1)
elevator = [up, -down]
floor_q = [initial_floor]
building[initial_floor] = 0
while floor_q:
    current_floor = floor_q.pop(0)
    for button in elevator:
        after_floor = current_floor + button
        if 1 <= after_floor <= top_floor and (building[after_floor] == -1 or building[after_floor] > building[current_floor] + 1):
            building[after_floor] = building[current_floor] + 1
            floor_q.append(after_floor)
if building[target_floor] != -1:
    print(building[target_floor])
else:
    print('use the stairs')
