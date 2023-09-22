import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

from collections import deque

for num in range(test_case):
    return_value = 0
    start, end = map(int, input().split())
    dic = {start : True}
    que = deque()
    que.append((start, 0))
    while que:
        next, ct = que.popleft()
        if next == end:
            return_value = ct
            break
        if next + 1 not in dic and next + 1 < 1e6:
            dic[next + 1] = True
            que.append((next + 1, ct + 1))
        if next - 1 not in dic and next - 1 > 0:
            dic[next - 1] = True
            que.append((next - 1, ct + 1))
        if next * 2 not in dic and next * 2  < 1e6:
            dic[next * 2] = True
            que.append((next * 2, ct + 1))
        if next - 10 not in dic and next - 10 > 0:
            dic[next - 10] = True
            que.append((next - 10, ct + 1))
    print(f'#{num + 1} {return_value}')