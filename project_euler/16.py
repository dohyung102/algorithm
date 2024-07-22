"""
215 = 32768 의 각 자릿수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

2 ** 1000의 각 자릿수를 모두 더하면 얼마입니까?
"""

from functools import reduce

print(reduce(lambda x, y: x + y, map(int, str(2 ** 1000))))