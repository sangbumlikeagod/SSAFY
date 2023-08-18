import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
from collections import deque

for num in range(test_case):
    return_value = 0
    V, E = map(int, input().split())
    dic = {}
    for _ in range(E):
        A, B = map(int, input().split())
        dic[A] = dic.get(A, []) + [B]
        dic[B] = dic.get(B, []) + [A]
    # print(dic)
    S, G = map(int, input().split())
    que = deque()
    que.append((S, 0))
    V = [0] * 51


    while que:
        get, idx = que.popleft()
        if get == G:
            return_value = idx
            break
        V[get] = 1
        for i in dic[get]:
            if not V[i]:
                que.append((i, idx + 1))



    print(f'#{num + 1} {return_value}')