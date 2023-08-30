import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

for num in range(test_case):
    dic = {}
    return_value = ''
    for _ in range(5):
        lst = list(input())
        for i in range(len(lst)):
            dic[i] = dic.get(i, '') + lst[i]
    i = 0
    while i in dic:
        return_value += dic[i]
        i += 1
    print(f'#{num + 1} {return_value}')