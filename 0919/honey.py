import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


def find_branch(idx, val, remain):
    if not remain:
        global maxx
        maxx = max(maxx, val)
        return

    if idx >= N:
        return
    
    possible = []

    for i in range(M - 1, N):
        tmp = []
        while i < N and len(tmp) < 2:
            tmp.append(i)
            possible.append(tmp[:])
            i += M
    
    for partial in possible:
        if len(partial) == 2 and remain == 2:
            this = 0
            for i in partial:
                if sum(lst[idx][i - M + 1: i + 1]) <= C:
                    this += sum(map(lambda i: i ** 2, lst[idx][i - M + 1: i + 1]))
                else:
                    this += findmax(lst[idx][i - M + 1: i + 1])
            find_branch(idx + 1, val + this, remain - 2)

        else:
            this = 0
            if sum(lst[idx][partial[0] - M + 1: partial[0] + 1]) <= C:
                this = sum(map(lambda i: i ** 2, lst[idx][partial[0] - M + 1: partial[0] + 1]))
            else:
                this = findmax(lst[idx][partial[0] - M + 1: partial[0] + 1])
            if val + this + C ** 2 >= maxx:
                for ps in range(idx + 1, N + 1):
                    find_branch(ps, val + this, remain - 1)



def findmax(lst):
    maxxt = 0
    for i in range((1 << len(lst)) - 1):
        local = 0
        local2 = 0
        for j in range(len(lst)):
 
            if i & 1 << j:
                local += lst[j]
                local2 += lst[j] ** 2
        if local <= C:
            maxxt = max(maxxt, local2)
    return maxxt



import heapq
for num in range(test_case):
    return_value = 0
    N, M, C = map(int, input().split())
    maxx = 0
    Max_row = N // M
    possible_max = (C - 1) ** 2 + 1
    lst = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        find_branch(i, 0, 2)
    print(f'#{num + 1} {maxx}')
