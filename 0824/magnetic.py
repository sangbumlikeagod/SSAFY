import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10


for num in range(test_case):
    return_value = 0
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    # print(table)
    for i in range(100):
        for j in range(100):
            if table[i][j] == 1:
                copy = i + 1
                while copy < 100 and table[copy][j] == 0:
                    copy += 1
                else:
                    if copy != 100 and table[copy][j] == 2:
                        # print(table[copy][j], copy)
                        table[copy][j] = 3
                        return_value += 1

                table[i][j] = 0

    print(f'#{num + 1} {return_value}')