import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 1


def search(vertex, llist):
    llist.append(vertex)
    dic_occupied[vertex] = 1
    if len(llist) == V:
        print(f"#{num + 1} {'-'.join(map(str, llist))}")
        return
    for i in dic[vertex]:
        if not dic_occupied[i]:
            search(i, llist)
    return




for num in range(test_case):

    V, E = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = {}
    dic_occupied = {}
    for i in range(0, E * 2, 2):
        dic[lst[i]] = dic.get(lst[i], []) + [lst[i + 1]]
        dic[lst[i + 1]] = dic.get(lst[i + 1], []) + [lst[i]]
        dic_occupied[lst[i]] = 0
        dic_occupied[lst[i + 1]] = 0
    search(1, [])

