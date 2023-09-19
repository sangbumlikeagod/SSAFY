import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

def quicksort(sst):
    if not sst:
        return []
    a = sst[0]
    left = []
    right = []
    mid = [a]
    for i in range(1, len(sst)):
        if sst[i] < a:
            left.append(sst[i])
        elif sst[i] > a:
            right.append(sst[i])
        else:
            mid.append(sst[i])
    return quicksort(left) + mid + quicksort(right)


for num in range(test_case):
    return_value = 0
    lst = list(map(int, input().split()))



    print(f'#{num + 1} {" ".join(map(str, quicksort(lst)))}')