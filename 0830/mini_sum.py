import sys
import heapq

name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

for num in range(test_case):
    return_value = 0
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    where = [(lst[0][0], (0, 0))]
    can_go = [[1, 0], [0, 1], [0, -1], [-1, 0]]
    idx = [0, 0]
    visted = [[0] * N for _ in range(N)]
    while idx[0] != N - 1 or idx[1] != N - 1:
        sumsum, idx = heapq.heappop(where)
        visted[idx[0]][idx[1]] = 1
        # print(sumsum, idx)
        for go in can_go:
            if 0 <= idx[0] + go[0] < N and 0 <= idx[1] + go[1] < N \
                    and not visted[idx[0] + go[0]][idx[1] + go[1]]:
                heapq.heappush(where, (sumsum + lst[idx[0] + go[0]][idx[1] + go[1]], (idx[0] + go[0], idx[1] + go[1])))
    print(f'#{num + 1} {sumsum}')