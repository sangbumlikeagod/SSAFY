import sys


name = __file__.split('\\')[-1][:-5]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
# test_case = 3


for num in range(test_case):
    return_value = 0
    N = [0] * 401
    students = int(input())
    for _ in range(students):
        a, b = map(int, input().split())
        if a > b: a, b = b, a
        if b % 2:
            b += 1
        if not a % 2:
            a -= 1
        for i in range(a, b + 2):
            N[i] += 1

    # print(N)
    # for i in
    print(f'#{num + 1} {max(N)}')