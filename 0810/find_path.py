

import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10


def search(idx):
    if idx in dic:
        for i in dic[idx]:
            if i == 99:
                return 1
            if not dic_for[i]:
                dic_for[i] == 1
                if search(i):
                    return 1

    return 0


for num in range(test_case):
    return_value = 0
    num, total = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = {}
    dic_for = {}



    for i in range(0, len(lst), 2):
        dic[lst[i]] = dic.get(lst[i], []) + [lst[i + 1]]
        dic_for[lst[i]] = 0
        dic_for[lst[i + 1]] = 0
    # print(dic)
    # print(dic_for)


    print(f'#{num} {search(0)}')