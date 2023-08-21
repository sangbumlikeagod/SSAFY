import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    E, N = map(int, input().split())
    lst_left = [0] * (E + 1)
    lst_right = [0] * (E + 1)

    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        if not lst_left[lst[i] - 1]:
            lst_left[lst[i] - 1] = lst[i + 1]
        else:
            lst_right[lst[i] - 1] = lst[i + 1]
    # print(lst_left, lst_right)


    def dfs(node):
        ans = 0
        if lst_left[node - 1]:
            ans += dfs(lst_left[node - 1])
        if lst_right[node - 1]:
            ans += dfs(lst_right[node - 1])
        return ans + 1


    return_value = dfs(N)






    print(f'#{num + 1} {return_value}')