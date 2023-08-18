import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


# 어디에 2가 있는지를 먼저 확인해야됨

def search(idx):
    if lst[idx[0]][idx[1]] == 3:
        return 1

    movable = [[idx[0] + i[0], idx[1] + i[1]] for i in [[1, 0], [0, 1], [-1, 0], [0, -1]] if 0 <= idx[0] + i[0] < length if 0 <= idx[1] + i[1] < length]
    # print(movable)
    for cord in movable:
        if lst[cord[0]][cord[1]] != 1:
            lst[idx[0]][idx[1]] = 1
            if search(cord):
                return 1
    return 0



for num in range(test_case):

    length = int(input())
    lst = [list(map(int, list(input()))) for _ in range(length)]
    print(lst)
    for i in range(length):
        for j in range(length):
            if lst[i][j] == 2:
                idx = [i, j]
    print(idx)
    return_value = search(idx)

    print(f'#{num + 1} {return_value}')