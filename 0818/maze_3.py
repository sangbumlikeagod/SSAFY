import sys
from collections import deque

name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                idx = [i, j]

    que = deque()

    #
    # def bfs(node, charge):
    #     # print(node)
    #     if maze[node[0]][node[1]] == 3:
    #         return charge - 1
    #     maze[node[0]][node[1]] = 1
    #     # print(maze[node[0]][node[1]])
    #     candidates = [[node[0] + i[0], node[1] + i[1]] for i in [[-1, 0], [1, 0], [0, 1], [0, -1]]\
    #                   if 0 <= node[0] + i[0] < N\
    #                   if 0 <= node[1] + i[1] < N\
    #                   if maze[node[0] + i[0]][node[1] + i[1]] != 1
    #                   ]
    #     # print(candidates)
    #     for candidate in candidates:
    #         que.append((candidate, charge + 1))
    #
    #     if not que:
    #         return 0
    #     else:
    #         a, b = que.popleft()
    #         return bfs(a, b)

    return_value = 0

    que.append((idx, 0))
    while que:
        node, idx = que.popleft()
        # print(node)
        if maze[node[0]][node[1]] == 3:
            return_value = idx - 1
            break
        maze[node[0]][node[1]] = 1
        candidates = [[node[0] + i[0], node[1] + i[1]] for i in [[-1, 0], [1, 0], [0, 1], [0, -1]]\
                      if 0 <= node[0] + i[0] < N\
                      if 0 <= node[1] + i[1] < N\
                      if maze[node[0] + i[0]][node[1] + i[1]] != 1
                      ]

        for candidate in candidates:
            que.append((candidate, idx + 1))
    print(f'#{num + 1} {return_value}')