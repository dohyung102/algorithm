import sys
sys.stdin = open('9019.txt')

def D(n):
    return 2 * n % 10000

def S(n):
    if n == 0:
        return 9999
    return n - 1

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return n // 10 + (n % 10) * 1000

commend_list = ['D', 'S', 'L', 'R']
T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    Q = [0]*10000
    start, end = -1, 0
    Q[end] = [A, '']
    maked = [False] * 10000
    maked[A] = True
    ans = 'N' * 10000
    while start < end:
        start += 1
        num, calc_commend = Q[start]
        for i in commend_list:
            if i == 'D':
                new_num = D(num)
            elif i == 'S':
                new_num = S(num)
            elif i == 'L':
                new_num = L(num)
            else:
                new_num = R(num)
            if new_num == B:
                if len(ans) > len(calc_commend) + 1:
                    ans = calc_commend + i
                continue
            if not maked[new_num] and len(calc_commend) + 1 < len(ans):
                maked[new_num] = True
                end += 1
                Q[end] = [new_num, calc_commend + i]
    print(ans)