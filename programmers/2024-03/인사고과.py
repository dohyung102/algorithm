def solution(scores):
    first_score_max = max(map(lambda x: x[0], scores))
    first_score_list = [[0, 0] for _ in range(first_score_max + 1)]
    first_score_exist = [0] * (first_score_max + 1)
    for score in scores:
        first_score_list[score[0]][0] = max(score[1], first_score_list[score[0]][0])
        first_score_exist[score[0]] = 1
    second_score_max = first_score_list[first_score_max][0]
    for score in range(first_score_max - 1, -1, -1):
        if first_score_exist[score]:
            first_score_list[score][1] = second_score_max
            second_score_max = max(first_score_list[score][0], second_score_max)
    wonho_total_score = sum(scores[0])
    if scores[0][0] == first_score_max:
        pass
    elif first_score_list[scores[0][0]][1] > scores[0][1]:
        return -1
    wonho_winner_count = 0
    for idx in range(1, len(scores)):
        score = scores[idx]
        if (score[0] == first_score_max or first_score_list[score[0]][1] <= score[1]) and sum(score) > wonho_total_score:
            wonho_winner_count += 1
    return wonho_winner_count + 1