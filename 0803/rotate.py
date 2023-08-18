import sys

file = open('rotate.txt', 'r')
sys.stdin = file

test_case = int(input())

def rotate(lst):
    N = len(lst)
    lst_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            lst_90[j][N - 1 - i] = lst[i][j]
    return lst_90


for num in range(test_case):
    N = int(input())
    lst2 = [list(input().split()) for _ in range(N)]

    # 90도
    re_lst1 = rotate(lst2)

    re_lst2 = rotate(re_lst1)

    re_lst3 = rotate(re_lst2)

    re_lst4 = [ ''.join(re_lst1[i]) + ' ' + ''.join(re_lst2[i]) + ' ' + ''.join(re_lst3[i]) for i in range(N) ]
    print(f'#{num}')
    for result in re_lst4:
        print( result )

    #




    #