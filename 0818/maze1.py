import sys
from queue import Queue

name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10


for num in range(test_case):
    test_case = int(input())
    return_value = 0
    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)
    # 출발점을 찾는다.

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                idx = [i, j]

    que = Queue()

    def bfs(node):
        if maze[node[0]][node[1]] == 3:
            return 1
        maze[node[0]][node[1]] = 1
        # print(maze[node[0]][node[1]])
        candidates = [[node[0] + i[0], node[1] + i[1]] for i in [[-1, 0], [1, 0], [0, 1], [0, -1]]\
                      if 0 <= node[0] + i[0] < 16\
                      if 0 <= node[1] + i[1] < 16\
                      if maze[node[0] + i[0]][node[1] + i[1]] != 1
                      ]
        # print(candidates)
        for candidate in candidates:

            que.put(candidate)

        if que.empty():
            return 0
        else:
            return bfs(que.get())

    print(f'#{num + 1} {bfs(idx)}')