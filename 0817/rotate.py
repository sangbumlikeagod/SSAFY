import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    # return_value = 0
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f'#{num + 1} {lst[M % N]}')