import sys

file = open('crossword.txt', 'r')
sys.stdin = file

test_case = int(input())
for num in range(test_case):
    result_value = 0
    N, K = map(int, input().split())
    lst_p2 = [list(map(int, input().split())) for _ in range(N)]

    for row in lst_p2:
        coutinuous = 0
        for arg in row:
            if arg:
                coutinuous += 1
            else:
                if coutinuous == K:
                    result_value += 1


                coutinuous = 0
        if coutinuous == K:


            result_value += 1


    for column in range(N):
        continuous = 0
        for row in range(N):

            if lst_p2[row][column]:
                continuous += 1
            else:
                if continuous == K:


                    result_value += 1
                continuous = 0

        if continuous == K:


            result_value += 1


    print(f'#{num + 1} {result_value}')