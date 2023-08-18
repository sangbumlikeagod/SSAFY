import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
test_case = 3

def permutation(row_now, row_end, column_now, column_end, s):

    global min_sofar
    if row_now == row_end or s >= min_sofar:
        if s < min_sofar:
            min_sofar = s
            # print(s)
        return s

    else:

        # print(A, s + A[row_now][column_now])
        a1 = permutation(row_now + 1, row_end, column_now + 1, column_end, s + A[row_now][column_now])
        if a1 < min_sofar:
            min_sofar = a1
        a2 = a1 + 1
        for j in range(column_now + 1, column_end):
            for row in range(row_now, row_end):
                A[row][column_now], A[row][j] = A[row][j], A[row][column_now]

            a2 = permutation(row_now + 1, row_end, column_now + 1, column_end, s + A[row_now][column_now])
            if a2 < min_sofar:
                min_sofar = a2
            for row in range(row_now, row_end):
                A[row][column_now], A[row][j] = A[row][j], A[row][column_now]
            # print(A, s + A[row_now][column_now])
        return min(a1, a2)

for num in range(test_case):
    min_sofar = 500
    size = int(input())
    A = [list(map(int, input().split())) for _ in range(size)]
    permutation(0, size, 0, size, 0)

    print(f'#{num + 1} {min_sofar}')

# 가장 겹치는 애를 빼주고