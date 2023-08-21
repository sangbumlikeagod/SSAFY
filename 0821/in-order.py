import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10


def dfs(node):
    global return_value
    # 왼쪽 이동
    if len(dic[node][1]) > 0:
        dfs(dic[node][1][0])
    # 출력
    return_value += (dic[node][0])
    # 오른쪽 이동
    if len(dic[node][1]) > 1:
        dfs(dic[node][1][1])


for num in range(test_case):
    size = int(input())
    return_value = ''
    dic = {}
    for _ in range(size):
        a, b, *c = input().split()
        dic[a] = (b, c)
    dfs('1')
    print(f'#{num + 1} {return_value}')