import sys

file = open('busstation.txt', 'r')
sys.stdin = file

test_case = int(input())
for num in range(test_case):
    dic = {}
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            dic[i] = dic.get(i, 0) + 1
    P = int(input())
    return_value = ''
    for _ in range(P):
        return_value += f'{dic.get(int(input()), 0)} '
    print(f'#{num + 1} {return_value}')