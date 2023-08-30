import sys
sys.setrecursionlimit(21473846)

name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file

test_case = int(input())
# test_case = 1


import heapq

#
# def search(idx):
#     next = [next for next in [[idx[0] + 1, idx[1] + 0], [idx[0] - 1, idx[1] + 0],
#                              [idx[0], idx[1] + 1], [idx[0], idx[1] - 1]] if 0 <= next[0] < N and 0 <= next[1] < N
#                             if lst[next[0]][next[1]] == lst[idx[0]][idx[1]] + 1]
#     if next:
#         next = next[0]
#         if visted[next[0]][next[1]]:
#             visted[idx[0]][idx[1]] = visted[next[0]][next[1]] + 1
#             return visted[next[0]][next[1]] + 1
#         else:
#             visted[idx[0]][idx[1]] = search(next) + 1
#             return visted[idx[0]][idx[1]]
#     else:
#         return 1


for num in range(test_case):
    return_value = 0
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visted = [[0] * N for _ in range(N)]
    where = []

    for i in range(N):
        for j in range(N):
            condition = True
            idx = [i, j]
            ans = 1
            while condition:
                to_go = [next for next in [[idx[0] + 1, idx[1] + 0], [idx[0] - 1, idx[1] + 0],
                                          [idx[0], idx[1] + 1], [idx[0], idx[1] - 1]] if
                        0 <= next[0] < N and 0 <= next[1] < N
                        if lst[next[0]][next[1]] == lst[idx[0]][idx[1]] + 1]
                if to_go:
                    next = to_go[0]
                    if visted[next[0]][next[1]]:
                        visted[idx[0]][idx[1]] = visted[next[0]][next[1]] + 1
                    idx = next
                    ans += 1
                else:
                    condition = False
            visted[i][j] = ans
            heapq.heappush(where, (-visted[i][j], lst[i][j]))


    # print(*visted, sep='\n')
    return_value = heapq.heappop(where)
    print(f'#{num + 1} {return_value[1]} {-return_value[0]}')