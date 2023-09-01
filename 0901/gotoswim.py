import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file

test_case = int(input())

from collections import deque

# def search(inner_idx):
#     # print(inner_idx)
    
#     for next in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#         # print(inner_idx[0] + next[0], inner_idx[1] + next[1])
#         if 0 <= inner_idx[0] + next[0] < N and 0 <= inner_idx[1] + next[1] < M and ocean[inner_idx[0] + next[0]][inner_idx[1] + next[1]] == 2000:
            
#             ocean[inner_idx[0] + next[0]][inner_idx[1] + next[1]] =  ocean[inner_idx[0]][inner_idx[1]] + 1
#             queue.append([inner_idx[0] + next[0], inner_idx[1] + next[1]])
#     if not queue:
#         return ocean[inner_idx[0]][inner_idx[1]]
#     return search(queue.popleft()) + ocean[inner_idx[0]][inner_idx[1]]

# di = [0, 0, -1, 1]
# dj = [1, -1, 0, 0]  

for num in range(1, test_case + 1):
    N, M = map(int,input().split())
    return_value = 0
    
    queue = []

    ocean = [[2000] * M for _ in range(N)]
    for i in range(N):
        local = list(input())
        for j in range(M):
            if local[j] == "W":
                ocean[i][j] = 0
                queue.append((i, j))
    idx = 0
    while idx < len(queue):
        inner_idx = queue[idx]
        return_value += ocean[inner_idx[0]][inner_idx[1]]
        for next in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= inner_idx[0] + next[0] < N and\
                0 <= inner_idx[1] + next[1] < M and\
                ocean[inner_idx[0] + next[0]][inner_idx[1] + next[1]] == 2000:
                ocean[inner_idx[0] + next[0]][inner_idx[1] + next[1]] =  ocean[inner_idx[0]][inner_idx[1]] + 1
                queue.append([inner_idx[0] + next[0], inner_idx[1] + next[1]])
        idx += 1


    # while queue :
    #     inner_idx = queue.popleft()
    #     return_value += ocean[inner_idx[0]][inner_idx[1]]
    #     for next in range(4):
    #         if 0 <= inner_idx[0] + di[next] < N and 0 <= inner_idx[1] + dj[next] < M and ocean[inner_idx[0] + di[next]][inner_idx[1] + dj[next]] == 2000:
    #             ocean[inner_idx[0] + di[next]][inner_idx[1] + dj[next]] =  ocean[inner_idx[0]][inner_idx[1]] + 1
    #             queue.append((inner_idx[0] + di[next], inner_idx[1] + dj[next]))

    print(f'#{num} {return_value}')



# test_case = int(input())
# for num in range(1, test_case + 1):
#     N, M = map(int,input().strip().split())
#     return_value = 0
#     queue = []
#     idx = 0
#     ocean = []
#     visited = [[2000] * M for _ in range(N)]
#     for i in range(N):
#         local = list(input().strip())
#         for j in range(M):
#             if local[j] == "W":
#                 visited[i][j] = 0
#                 queue.append([i, j])
#         ocean += [local]
#     while idx < len(queue) :
#         inner_idx = queue[idx]
#         for next in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#             if 0 <= inner_idx[0] + next[0] < N and 0 <= inner_idx[1] + next[1] < M and visited[inner_idx[0] + next[0]][inner_idx[1] + next[1]] == 2000:
#                 visited[inner_idx[0] + next[0]][inner_idx[1] + next[1]] =  visited[inner_idx[0]][inner_idx[1]] + 1
#                 queue.append([inner_idx[0] + next[0], inner_idx[1] + next[1]])
#         idx += 1
    
#     for i in visited:
#         return_value += sum(i)
        
#     print(f'#{num} {return_value}')