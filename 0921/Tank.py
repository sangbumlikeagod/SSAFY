import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
import heapq

for num in range(test_case):
    return_value = 0
    N = int(input())
    lst = [list(map(int, list(input()))) for _ in range(N)] 
    que = [(0, 0, 0)]
    visited = [[0] * N for _ in range(N)]

    while que:
        v, x, y = heapq.heappop(que)
        if x == N - 1 and y == N - 1:
            return_value = v
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                heapq.heappush(que, (v + lst[nx][ny], nx, ny))

    print(f'#{num + 1} {return_value}')