import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    return_value = 0
    N, value = input().strip().split()
    N = int(N)
    idx = 0
    ans = ''
    while N - 1 >= 0:
        # print(ans)
        if value[idx].isdigit():
            for i in range(3, -1, -1):
                ans += str((int(value[idx]) & 1 << i) // (1 << i))
        else:
            ABCD = 10 + ord(value[idx]) - ord('A')
            for i in range(3, -1, -1):
                ans += str((ABCD & 1 << i) // (1 << i))
        idx += 1
        N -= 1
    print(f'#{num + 1} {ans}')