import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

def rcp(in1, in2):
    rule = {1 : 2,
     2 : 3,
     3 : 1}
    if in1[1] == in2[1]:
        return in1
    elif rule[in1[1]] != in2[1]:
        return in1
    else:
        return in2

def dandq(lst):
    # print(lst)
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return rcp(lst[0], lst[1])
    return rcp(dandq(lst[:(lst[0][0] + lst[-1][0]) // 2 + 1 - lst[0][0]]), dandq(lst[(lst[0][0] + lst[-1][0]) // 2 + 1 - lst[0][0]:]))


for num in range(test_case):
    return_value = 0
    N = int(input())

    lst = [ i for i in enumerate(list(map(int, input().split())))]

    print(f'#{num + 1} {dandq(lst)[0] + 1}')