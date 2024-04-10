def solution(coin, cards):
    answer = 1
    target = len(cards) + 1
    hands = cards[ :len(cards) // 3]
    hands_count = len(hands)
    is_checked = [False] * target
    number_cost = [1] * target

    for number in hands:
        is_checked[number] = True
        number_cost[number] = 0
        if is_checked[target - number]:
            answer += 1


    start, end = hands_count, hands_count + 1 + answer * 2 - 2
    two_cost = 0
    while start <= end:
        
        number = cards[start]
        is_checked[number] = True
        if is_checked[target - number] and coin >= number_cost[target - number] + 1:
            if number_cost[target - number] + 1 == 2:
                print(number)
                two_cost += 1
            else:
                coin -= 1
                answer += 1
                end = min(len(cards) - 1, end + 2)           
        start += 1
        if start > end and end < len(cards) - 1 and coin > 1 and two_cost:
            two_cost -= 1
            coin -= 2
            end += 2
            answer += 1
    return answer
