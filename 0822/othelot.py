import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


def delta(position, type):
    i = type[0]
    i2 = type[1]
    b = 1
    while 0 <= position[0] + i * b < len(lst) and 0 <= position[1] + i2 * b < len(lst) and lst[position[0] + i * b][position[1] + i2 * b] != 0 and lst[position[0] + i * b][position[1] + i2 * b] != lst[position[0]][position[1]]:
        b += 1
    else:
        if 0 <= position[0] + i * b < len(lst) and 0 <= position[1] + i2 * b < len(lst) and lst[position[0] + i * b][position[1] + i2 * b] == lst[position[0]][position[1]]:
            # print(i, i2, b)
            for j in range(1, b):
                lst[position[0] + i * j][position[1] + i2 * j] = lst[position[0]][position[1]]


for num in range(test_case):

    N, M = map(int, input().split())
    # 입력이 주어지면
    lst = [[0] * N for _ in range(N)]
    lst[N // 2 - 1][N // 2 - 1], lst[N // 2][N // 2], lst[N // 2][N // 2 - 1], lst[N // 2 - 1][N // 2] = 2, 2, 1, 1
    # print([[i, j] for i in [-1, 1] for j in [-1,1]])
    # 돌을 놓기, 놓고나서 4방향 모두에 대해서 델타 탐색을 조져
    for i in range(M):
        a, b, c = map(int, input().split())
        lst[a - 1][b - 1] = c

        # for i in range(N):
        #     print(lst[i])

        for moving in [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1]]:
            delta((a - 1, b - 1), moving)
        # for i in range(N):
        #     print(lst[i])
        # print()

    # 다 끝났다 세보자
    black = white = 0
    for o in range(N):
        for j in range(N):
            if lst[o][j] == 2:
                white += 1
            elif lst[o][j]:
                black += 1


    print(f'#{num + 1} {black} {white}')