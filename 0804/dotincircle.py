import sys

file = open('dotincircle.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):

    N = int(input())
    return_value = 0
    for i in range(N):
        return_value += int((N ** 2 - i ** 2) ** (1/2))

    print(f'#{num + 1} {return_value * 4 + 1}')