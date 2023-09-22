import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
import heapq

for num in range(test_case):
    return_value = 0
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    que = [(0, 0, 0)]
    visited = [[- 1] * N for _ in range(N)]
    visited[0][0] = lst[0][0]
    while que:
        v, nx, ny = heapq.heappop(que)
        if nx == N - 1 and ny == N - 1:
            return_value = v
            break
        for i in range(4):
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if 0 <= nnx < N and 0 <= nny < N and visited[nnx][nny] < lst[nx][ny]:
                visited[nnx][nny] = lst[nx][ny]
                heapq.heappush(que, (max(lst[nnx][nny] - lst[nx][ny], 0) + 1 + v, nnx, nny))
    



    print(f'#{num + 1} {return_value}')