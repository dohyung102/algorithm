import sys
sys.stdin = open('12865.txt')

number_of_item, weight_limit = map(int, input().split())
value_by_weight = [0] * (weight_limit + 1)
for item in range(number_of_item):
    item_weight, item_value = map(int, input().split())
    if item_weight <= weight_limit:
        for index in range(weight_limit - item_weight, 0, -1):
            if value_by_weight[index] and value_by_weight[index] + item_value > value_by_weight[index + item_weight]:
                value_by_weight[index + item_weight] = value_by_weight[index] + item_value
        if item_value > value_by_weight[item_weight]:
            value_by_weight[item_weight] = item_value
print(max(value_by_weight))

