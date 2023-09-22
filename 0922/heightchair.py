import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

def search(bitt, idx, val):
    # if num == 3:
    #     print(bin(bitt), idx, val)
    if val >= B:
        global minn
        minn = min(minn, val)
        return
    if not bitt:
        return 
    search(bitt  - (1 << idx) , idx + 1, val)
    if val + lst[idx] < minn:
        search(bitt - (1 << idx), idx + 1, val + lst[idx])

    


for num in range(test_case):
    return_value = 0
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    minn = float('inf')
    search( (1 << N) - 1, 0, 0)

    print(f'#{num + 1} {minn - B}')
    # break