def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        ball_x = ball[0]
        ball_y = ball[1]
        distances = []
        if not (startY == ball_y and startX > ball_x):
            distances.append(pow(startX + ball_x, 2) + pow(startY - ball_y, 2))
        if not (startY == ball_y and startX < ball_x):
            distances.append(pow(startX + ball_x - 2 * m, 2) + pow(startY - ball_y, 2))
        if not (startX == ball_x and startY > ball_y):
            distances.append(pow(startX - ball_x, 2) + pow(startY + ball_y, 2))
        if not (startX == ball_x and startY < ball_y):
            distances.append(pow(startX - ball_x, 2) + pow(startY + ball_y - 2 * n, 2))
        answer.append(min(distances))
    return answer