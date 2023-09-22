import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


# 모든 순열에 대해서 해야하는 문제지만 그거보다 낮을 때 할 수 있음.
def dfs(num, ssum, ct):
    # print(num, ssum)
    global minimi
    if num == 0:
        minimi = min(ssum, minimi)
    for i in range(N):
        if num & 1 << i and ssum + NbyN[ct][i] < minimi:
            dfs(num - (1 << i), ssum + NbyN[ct][i], ct + 1)
    




for num in range(test_case):
    N = int(input())
    return_value = 0
    NbyN = [list(map(int, input().split())) for _ in range(N)]

    minimi = float('inf')

    dfs((1 << N) - 1, 0, 0)
    # print(minimi)
    print(f'#{num + 1} {minimi}')