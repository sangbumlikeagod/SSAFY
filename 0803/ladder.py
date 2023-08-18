import sys

file = open('ladder.txt', 'r')
sys.stdin = file

test_case = 10
# sys.setrecursionlimit(1000000)

num = 0
while num < test_case:
    int(input())
    ladder = [ list(map(int, input().split())) for _ in range(100) ]
    b = 0
    for last_row in ladder[99]:
        if last_row == 2:
            break
        else:
            b += 1
    a = 99
    while a > 0:
        if b > 0 and ladder[a][b - 1]:
            ladder[a][b] = 0
            b -= 1
            continue
        elif b < 99 and ladder[a][b + 1]:
            ladder[a][b] = 0
            b += 1
            continue
        else:
            a -= 1
            continue
    # print(idx)
    num += 1
    print(f'#{num} {b}')