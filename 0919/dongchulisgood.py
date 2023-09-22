import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

'''
N 명이니까 10 ^ n 만큼 나누어줘야 하는데 엄청커서 안되겠다

'''

def search(state, pro, now):
    # print(state)
    if not state:
        global biggie
        biggie = max(biggie, pro)
    for i in range(N):
        if state & (1 << i) and NbyN[i][now] != 0 and pro * NbyN[i][now] * 0.01 > biggie:
            search(state - (1 << i), pro * NbyN[i][now] * 0.01, now + 1)


for num in range(test_case):
    N = int(input())
    biggie = 0
    NbyN = [list(map(int, input().split())) for _ in range(N)]
    search((1 << N) - 1, 1, 0)
    # print(biggie)
    print(f'#{num + 1}',"{:.6f}".format(round(biggie * 100, 6)))
    # break