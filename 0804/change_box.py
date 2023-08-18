import sys

file = open('change_box.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    # 숫자를 반영
    N, Q = map(int, input().split())
    n = [0] * N
    for _ in range(Q):
        i, j = map(int, input().split())
        for k in range(i-1, j):
            n[k] = _ + 1

    return_value = " ".join(map(str, n))

    print(f'#{num + 1} {return_value}')