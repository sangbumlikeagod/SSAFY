

def bfs(sti, stj, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j] - 2 # 여기서 1을 리턴하겠다 ? 아니면 0 리턴 할 거고
        for di, dj in [[0, 1], [1, 0],[0, -1], [-1, 0]]:
            ni, nj = i + di, i + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


