import sys

file = open('snail.txt', 'r')
sys.stdin = file

test_case = int(input())
def selection_sort(secondary_lst):
    len_lst = len(secondary_lst) * len(secondary_lst[0])
    size = len(secondary_lst)
    idx = 0
    while idx < len_lst:
        mind = 1000000
        min_idx = 0
        for i in range(idx, len_lst):
            if secondary_lst[i // size][i % size] < mind:
                mind = secondary_lst[i // size][i % size]
                min_idx = i
        secondary_lst[idx // size][idx % size] , secondary_lst[min_idx // size][min_idx % size] = secondary_lst[min_idx // size][min_idx % size] , secondary_lst[idx // size][idx % size]
        idx += 1
    return secondary_lst


for num in range(test_case):
    row_column = int(input())

    power_lst = [ list(map(int, input().split())) for _ in range(row_column) ]

    sorted_list = selection_sort(power_lst)
    first_lst = []
    for i in sorted_list:
        first_lst += i
    snail = [[0] * row_column for i in range(row_column)]
    row, column = 0, -1
    while first_lst:

        for i in range(row_column):
            if first_lst:
                column += 1
                snail[row][column] = first_lst.pop(0)
            else:
                break

        for i in range(row_column - 1):
            if first_lst:
                row += 1
                snail[row][column] = first_lst.pop(0)
            else:
                break

        for i in range(row_column - 1):
            if first_lst:
                column -= 1
                snail[row][column] = first_lst.pop(0)
            else:
                break

        for i in range(row_column - 2):
            if first_lst:
                row -= 1
                snail[row][column] = first_lst.pop(0)
            else:
                break

        row_column -= 2




    print(f'#{num + 1}')
    for i in snail:
        print(' '.join(map(str, i)))