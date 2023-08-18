import sys

file = open('whereword.txt', 'r')
sys.stdin = file

test_case = int(input())
for num in range(test_case):
    N, K = map(int, input().split())
    power_lst = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for row in power_lst:
        idx = 0
        continueous_1 = 0
        while idx < N:
            if row[idx]:
                continueous_1 += 1
            else:
                if continueous_1 == K:
                    count += 1
                continueous_1 = 0
            idx += 1
        if continueous_1 == K:
            count += 1

    for column in range(N):
        idx = 0
        continueous_1 = 0
        while idx < N:
            if power_lst[idx][column]:
                continueous_1 += 1
            else:
                if continueous_1 == K:
                    count += 1
                continueous_1 = 0
            idx += 1
        if continueous_1 == K:
            count += 1
    print(f'#{num + 1} {count}')