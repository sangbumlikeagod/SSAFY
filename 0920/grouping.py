import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

def find(a):
    if which_team[a] != a:
        a = find(which_team[a])
    return a

def searchh(a, b):
    which_team[max(a, b)] = min(a, b)
    return

for num in range(test_case):
    return_value = set()
    N, M = map(int, input().split())
    which_team = list(range(N + 1))
    lst = list(map(int, input().split()))
    for i in range(M):
        a, b = lst[i * 2], lst[i * 2 + 1]
        searchh(find(a), find(b))
    for i in which_team:
        return_value.add(find(i))
    # print(set(which_team), which_team)
    print(f'#{num + 1} {len(return_value) - 1}')