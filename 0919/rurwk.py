import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


# 격자에서 다시 왔다갔다 해도 된다라
# 무언가 저장을 확실히 해줘야함 그냥 한번 갔다고 해주면 안됨
# 그 자리 그대로에 힘이 있다
# 

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for num in range(test_case):
    return_value = set()
    real_gangster = [input().split() for _ in range(4)]
    visited = [[set(real_gangster[j][i]) for i in range(4)] for j in range(4)]
    print(*visited, sep='\n')
    for i in range(6):
        for p in range(4):
            for k in range(4):
                for arg in visited[p][k]:
                    for what in range(4):
                        nx, ny = p + dx[what], k + dy[what]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            new_word = arg + real_gangster[nx][ny]
                            if len(new_word) == 7:
                                return_value.add(new_word)
                            else:
                                visited[p + dx[what]][k + dy[what]].add(arg + real_gangster[p + dx[what]][k + dy[what]])
    # print(visited)
    print(f'#{num + 1} {len(return_value)}')