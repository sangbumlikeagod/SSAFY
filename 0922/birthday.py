import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
sys.setrecursionlimit(1000000)

# def move(start, end):
#     stack = [start]
#     visited = [0] * (N + 1)
#     visited[0] = 1
#     visited[start] = 1
#     val = 0
#     maxx = float('inf')
#     while stack:
#         # print(stack, visited)
#         now = stack[-1]
#         if now == end:
#             maxx = min(val, maxx)
#             tmp = stack.pop()
#             if stack:
#                 val -= lst[stack[-1]][tmp]
#             continue
#         # if lst[now]:
#         for _ in range(1, 5):
#             # print(_)

#             if not visited[_]:
#                 visited[_] = 1
#                 stack.append(_)
#                 val += lst[now][_]
#                 break
#         else:
#             tmp = stack.pop()
#             if stack:
#                 val -= lst[stack[-1]][tmp]

#         # else:
#         #     tmp = stack.pop()
#         #     if stack:
#         #         val -= lst[stack[-1]][tmp]

#     return maxx

def seach(now, end):
    # print(now, end)
    if now == end:
        return 0
    if (now, end) in dic:
        return dic[(now, end)]
    else:
        ret = []
        for i in lst[now]:
            if not visited[i[1]]:
                visited[i[1]] = 1
                ret.append(seach(i[1], end) + i[0])
                visited[i[1]] = 0
        dic[(now, end)] = float('inf') if not ret else min(ret)
        return dic[(now, end)]



for num in range(test_case):
    return_value = 0
    N, M, X = map(int, input().split())
    lst = [[] for _ in range(N + 1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        lst[x].append((c, y))
    dic = {}
    maxt = 0
    for i in range(1, N + 1):
        if i != X:
            visited = [0] * (N + 1)
            a = seach(i, X)
            b = seach(X, i)
            # print(dic)
            if a + b != float('inf'):
                maxt = max(a + b, maxt)
    print(f'#{num + 1} {maxt}')
    # break