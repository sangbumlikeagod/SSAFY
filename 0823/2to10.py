import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    N = int(input())
    long = ''
    for _ in range(N):
        long += input().strip()
    print(f'#{num + 1}', end= ' ')
    for _ in range(1, 11):
        idx = 7 * _
        local = 0
        for k in range(1, 8):
            local += int(long[idx - k]) << k - 1
        print(local, end = ' ')



