import sys

file = open('ladder.txt', 'r')
sys.stdin = file

test_case = 10
# sys.setrecursionlimit(1000000)

num = 0
while num < test_case:
    int(input())
    ladder = [ list(map(int, input().split())) for _ in range(100) ]

    for i in range(100):
        a, b = 0, i
        if not ladder[a][b]:
            continue
        prev_x, prev_y = -1, -1
        # print('\t\t\t\t\t', i)
        while a < 99:


            if b > 0 and ladder[a][b - 1] and not (a == prev_x and b - 1 == prev_y):
                # print('move 왼쪽')
                # print(prev_x, prev_y)
                prev_x, prev_y = a, b
                b -= 1

            elif b < 99 and ladder[a][b + 1] and not (a == prev_x and b + 1 == prev_y):

                # print(prev_x, prev_y)
                # print('move 오른쪽')
                prev_x, prev_y = a, b
                b += 1
            else:
                # print(prev_x, prev_y)
                # print('move 아래')
                prev_x, prev_y = a, b

                a += 1
        # print(a, b)
        if ladder[a][b] == 2:
            break
        else:
            continue



    # print(idx)
    num += 1
    print(f'#{num} {i}')