import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


# 1 10 100 0 0 0 0 0 0 ... 을 생각하면 
'''



'''
def letsgo(idx, chance):   
    # print(idx)
    if idx + lst[idx] >= m - 1:
        global minimi
        minimi = min(minimi, chance)
    else:
        if chance < minimi:
            for i in range(lst[idx], 0, -1):
                letsgo(idx + i, chance + 1)


for num in range(test_case):
    m, *lst = list(map(int, input().split()))
    minimi = float('inf')
    letsgo(0, 0)
    print(f'#{num + 1} {minimi}')