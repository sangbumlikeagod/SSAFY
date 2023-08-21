import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 1


for num in range(test_case):
    V = int(input())
    lst = list(map(int, input().split()))
    dic = {}
    for i in range(0, 2 * (V - 1), 2):
        dic[lst[i]] = dic.get(lst[i], []) + [lst[i + 1]]
    def dfs(node):
        print(node, end=' ')
        for i in dic.get(node, []):
            dfs(i)
    dfs(1)









    # print(f'#{num + 1} {return_value}')