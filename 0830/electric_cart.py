import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
def search(integer, where):
    if integer == 0:
        return [lst[where][0]]
    ans = []
    for i in range(N):
        if 1 << i & integer:
            sub_lst = search(integer - (1 << i), i)
            for small in sub_lst:
                ans += [small + lst[where][i]]
    return ans
for num in range(test_case):
    N = int(input())
    lst = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [0] * N
    pointer = 0
    print(f'#{num + 1} {min(search(2 ** N - 2, 0))}')




