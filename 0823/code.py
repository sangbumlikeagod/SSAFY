import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
# test_case = 1


for num in range(test_case):
    return_value = 0
    N, M = map(int, input().split())
    lst = list(input() for _ in range(N))
    idx = 0
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if lst[i][j] == '1':
                idx = [i, j]
                break
        if idx != 0: break
    dic = {
        13 : 0,25 : 1,19 : 2,61 : 3,35 : 4,49 : 5,47 : 6,59 : 7,55 : 8,11 : 9
    }
    return_even = 0
    return_odd = 0
    for i in range(8):
        local = 0
        ss = 0
        for j in range(7):
            local += int(lst[idx[0]][idx[1]]) * (1 << ss)
            ss += 1
            idx[1] -= 1
        if not i % 2:
            return_even += dic[local]
        else:
            return_odd += dic[local]
    if (return_even + return_odd * 3) % 10 == 0:
        return_value = return_odd + return_even
    print(f'#{num + 1} {return_value}')