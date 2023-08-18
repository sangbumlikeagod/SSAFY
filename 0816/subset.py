
import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r', encoding = 'utf-8')
sys.stdin = file



def f(i, N, t, s):
    global cnt

    if s == t:
        cnt += 1
        return 1
    if i == N:
        return 0
    elif s > t:
        return 0
    else:
        return f(i + 1, N, t, s) + f(i + 1, N, t, s + A[i])


for i in range(1, 2):
    cnt = 0
    A = list(map(int, input().split()))
    print(f'#{i} {f(0, 10, 10, 0)}')