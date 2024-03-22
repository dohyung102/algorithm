def solution(land):
    answer = 0
    width, depth = len(land[0]), len(land)
    direction = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
    ]
    total_remained = sum(map(sum, land))
    oil_amount_list = [0] * width
    for column in range(width):
        if answer < oil_amount_list[column] + total_remained:
            for row in range(depth):            
                if land[row][column]:
                    connected_column = set()
                    amount = 0
                    queue = [[row, column]]
                    land[row][column] = 0
                    start, end = 0, 1
                    while start < end:
                        current_row, current_col = queue[start]
                        start += 1
                        connected_column.add(current_col)
                        amount += 1
                        for dir in range(4):
                            new_row, new_col = current_row + direction[dir][0], current_col + direction[dir][1]
                            if 0 <= new_col < width and 0 <= new_row < depth and land[new_row][new_col]:
                                land[new_row][new_col] = 0
                                queue.append([new_row, new_col])
                                end += 1
                    for c_column in connected_column:
                        oil_amount_list[c_column] += amount
                        answer = max(oil_amount_list[column], answer)
                    total_remained -= amount
                    if not total_remained:
                        return answer
        else:
            return answer
    return answer