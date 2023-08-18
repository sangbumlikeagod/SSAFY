import sys

file = open('psudocu.txt', 'r')
sys.stdin = file

test_case = int(input())


def array_sum(arr):
    # print(arr)
    for i in range(1,10):
        if i not in arr:
            # print('\t\t',arr)
            return False
    return True


for num in range(test_case):
    lst = [list(map(int, input().split())) for _ in range(9)]

    switch = 1
    for i in range(9):
        if not array_sum(lst[i]):
            print('행에서')
            switch = 0
            break
        if not array_sum([lst[k][i] for k in range(9)]):
            print('열에서')
            switch = 0
            break
    else:
        print('뭐야')
        if not switch:
            print(f'#{num + 1} 0')
            continue




    for cord in [[i, j] for i in range(3) for j in range(3)]:
        # print([lst[cord[0] * 3 + i][cord[1] * 3 + j] for i in range(3) for j in range(3)])
        if not array_sum([lst[cord[0] * 3 + i][cord[1] * 3 + j] for i in range(3) for j in range(3)]):
            switch = 0
            print('대각선에서')
            break
    else:
        print('넌 왜 돼')
        if not switch:
            print(f'#{num + 1} 0')
            continue


    print('으헿')
    print(f'#{num + 1} 1')