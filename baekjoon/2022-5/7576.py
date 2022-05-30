dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_tomato(s, e):
    global remain_tomato_cnt
    while s < e:
        s += 1
        c, r = q[s]
        for i in range(4):
            cur_c, cur_r = c + dc[i], r + dr[i]
            if 0 <= cur_c < col and 0 <= cur_r < row:
                if tomato_farm[cur_c][cur_r] == 0:
                    tomato_farm[cur_c][cur_r] = tomato_farm[c][r] + 1
                    remain_tomato_cnt -= 1
                    e += 1
                    q[e] = (cur_c, cur_r)


row, col = map(int, input().split())
tomato_farm = [list(map(int, input().split())) for _ in range(col)]
front = end = -1
q = [0] * row * col
remain_tomato_cnt = 0
for c in range(col):
    for r in range(row):
        if tomato_farm[c][r] == 1:
            end += 1
            q[end] = (c, r)
        elif tomato_farm[c][r] == 0:
            remain_tomato_cnt += 1
if not q:
    print(-1)
else:
    find_tomato(front, end)
    if remain_tomato_cnt:
        print(-1)
    else:
        ans = 0
        for lst in tomato_farm:
            lst_max = max(lst)
            if lst_max > ans:
                ans = lst_max
        print(ans-1)