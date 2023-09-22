import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


def search(month, val):
    if month >= 12:
        global minn
        minn = min(minn, val)
        return
    if not lst[month]:
        search(month + 1, val)
    if lst[month] * daily > monthly:
        if monthly + val < minn:
            search(month + 1, val + monthly)
        if quarterly + val < minn:
            search(month + 3, val + quarterly)
    else: 
        if lst[month] * daily + val < minn:
            search(month + 1, val + lst[month] * daily)
        if quarterly + val < minn:
            search(month + 3, val + quarterly)



for num in range(test_case):
    return_value = 0
    daily, monthly, quarterly, annually = map(int, input().split())
    minn = annually
    lst = list(map(int, input().split()))
    # print(lst)
    search(0, 0)
    print(f'#{num + 1} {minn}')