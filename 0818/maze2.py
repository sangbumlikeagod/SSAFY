import sys
from queue import Queue
from collections import deque
sys.setrecursionlimit(1000000)
name = __file__.split('\\')[-1][:-3]

file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10


for num in range(test_case):
    test_case = int(input())
    return_value = 0
    maze = [list(map(int, input())) for _ in range(100)]

    # 출발점을 찾는다.

    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                idx = [i, j]
    # for i in range(100):
    #     for j in range(100):
    #         if maze[i][j] == 3:
    #             print([i, j])
    # print(idx)
    que = deque()
    que.append(idx)
    while que:
        node = que.popleft()
        # print(node)
        if maze[node[0]][node[1]] == 3:
            return_value = 1
            break
        maze[node[0]][node[1]] = 1
        candidates = [[node[0] + i[0], node[1] + i[1]] for i in [[-1, 0], [1, 0], [0, 1], [0, -1]]\
                      if 0 <= node[0] + i[0] < 100\
                      if 0 <= node[1] + i[1] < 100\
                      if maze[node[0] + i[0]][node[1] + i[1]] != 1
                      ]

        for candidate in candidates:
            que.append(candidate)


    # def bfs(node):
    #     # print(node)
    #     if maze[node[0]][node[1]] == 3:
    #         return 1
    #     maze[node[0]][node[1]] = 1
    #     # print(maze[node[0]][node[1]])
    #     candidates = [[node[0] + i[0], node[1] + i[1]] for i in [[-1, 0], [1, 0], [0, 1], [0, -1]]\
    #                   if 0 <= node[0] + i[0] < 100\
    #                   if 0 <= node[1] + i[1] < 100\
    #                   if maze[node[0] + i[0]][node[1] + i[1]] != 1
    #                   ]
    #     # print(candidates)
    #     for candidate in candidates:
    #
    #         que.append(candidate)
    #
    #     if not que:
    #         return 0
    #     else:
    #         return bfs(que.popleft())


    print(f'#{num + 1} {return_value}')