import sys

file = open('popballoon.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    row, column = map(int, input().split())
    lst = [ list(map(int, input().split())) for _ in range(row) ]

    return_value = 0

    for _ in range(row):
        for __ in range(column):
            local_sum = lst[_][__]
            for i in [[_ + i, __ + j] for i, j in [[-1, 0], [0, 1], [0, -1], [1, 0]] if 0 <= _ + i < row if 0<= __ + j < column ]:
                local_sum += lst[i[0]][i[1]]

            if local_sum > return_value:
                return_value = local_sum






    print(f'#{num + 1} {return_value}')