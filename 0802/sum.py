import sys

file = open('sum.txt', 'r')
sys.stdin = file



def sum(arr):
    ans = 0
    for i in arr:
        ans += i
    return ans


test_case = 10


for _ in range(test_case):
    case_num = int(input())
    power_arr = [list(map(int, input().split())) for _ in range(100)]

    row_sum = 0
    for row in power_arr:
        local_sum = sum(row)
        if row_sum < local_sum:
            row_sum = local_sum

    column_sum = 0
    for column in range(100):
        local_sum = sum([power_arr[k][column] for k in range(100)])
        if local_sum > column_sum:
            column_sum = local_sum

    sum_by_far = column_sum if column_sum > row_sum else row_sum

    left_diagonal = sum([power_arr[i][i] for i in range(100)])
    right_diagonal = sum([power_arr[i][99 - i] for i in range(100)])
    diagonal_sum = left_diagonal if left_diagonal > right_diagonal else right_diagonal
    total_sum = sum_by_far if sum_by_far > diagonal_sum else diagonal_sum

    print(f'#{case_num} {total_sum}')
