import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10
from collections import  deque

for num in range(test_case):
    L, S = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = {}
    for i in range(0, L, 2):
        dic[lst[i]] = dic.get(lst[i], set()) | {lst[i + 1]}

    V = {}
    que = deque()
    que.append((S, 0))
    max_idx, max_get = 0, 0
    while que:
        get, idx = que.popleft()
        if idx > max_idx:
            max_idx = idx
            max_get = get
        elif idx == max_idx:
            if get > max_get:
                max_idx = idx
                max_get = get

        V[get] = 1
        if get in dic:
            for i in dic[get]:
                if i not in V:
                    V[i] = 1
                    que.append((i, idx + 1))

    print(f'#{num + 1} {max_get}')