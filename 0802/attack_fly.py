import sys

file = open('attack_fly.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    return_value = 0
    N, M = map(int, input().split())
    fly_where = [list(map(int, input().split())) for _ in range(N)]
    catcher = [ [i, j] for i in range(0, M) for j in range(0, M) ]
    # print(catcher)
    for row in range(N - M + 1):
        for column in range(N - M + 1):
            local_sum = 0

            fly_count = [fly_where[row + cord[0]][column + cord[1]] for cord in catcher]
            # print(fly_count)
            for i in fly_count:
                local_sum += i
            if local_sum > return_value:
                return_value = local_sum






    print(f'#{num + 1} {return_value}')