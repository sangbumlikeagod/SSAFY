import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    return_value = 1
    dfdf = int(input())
    lst = []
    for i in range(dfdf):
        lst.append(tuple(map(int, input().split())))
    # print(lst)
    lst.sort(key= lambda x: x[0])
    lst.sort(key= lambda x: x[1])
    init = 0
    for i in range(1, len(lst)):
        if lst[i][0] >= lst[init][1]:
            init = i
            return_value += 1





    print(f'#{num + 1} {return_value}')