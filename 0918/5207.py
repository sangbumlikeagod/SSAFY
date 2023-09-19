import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


def binarysearch(start, end, before, target):

    # print(start, end)
    if end < start:
        return 0
    
    mid = (start + end) // 2
    if lst1[mid] == target:
        return 1
    elif lst1[mid] < target:
        # 전에도 왼쪽이었으면 
        if before == 1:
            return 0
        return binarysearch(mid + 1, end, 1, target)
    else:
        # 전에도 오른쪽이었으면
        if before == 2:
            return 0
        return binarysearch(start, mid - 1, 2, target)


for num in range(test_case):
    return_value = 0
    A, B = map(int, input().strip().split())
    lst1 = list(map(int, input().strip().split()))
    lst2 = list(map(int, input().strip().split()))
    dic = {}
    for i in lst2:
        if i in dic:
            return_value += dic[i]
        else:
            dic[i] =  binarysearch(0, A - 1, 0, i)
            return_value += dic[i]

    print(f'#{num + 1} {return_value}')