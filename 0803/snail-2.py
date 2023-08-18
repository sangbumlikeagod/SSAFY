import sys

file = open('snail-2.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):

    N = int(input())

    if N == 1:
        print(f'#{num + 1}')
        print(1)
        continue

    idx = 1
    snail = [[0] * N for i in range(N)]

    row = 0
    column = -1
    len_snail = N ** 2 + 1
    while idx < len_snail:

        for i in range(N):
            if idx < len_snail ** 2:
                column += 1
                snail[row][column] = idx
                idx += 1

            else:
                break
        # print(snail)
        for i in range(N - 1):
            if idx < len_snail ** 2:
                row += 1
                snail[row][column] = idx
                idx += 1
            else:
                break

        for i in range(N - 1):
            if idx < len_snail ** 2:
                column -= 1
                snail[row][column] = idx
                idx += 1
            else:
                break

        for i in range(N - 2):
            if idx < len_snail ** 2:
                row -= 1
                snail[row][column] = idx
                idx += 1
            else:
                break

        N -= 2




    print(f'#{num + 1}')
    for i in snail:
        print(' '.join(map(str, i)))