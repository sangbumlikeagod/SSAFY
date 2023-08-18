
import sys

file = open('pascal.txt', 'r')
sys.stdin = file

test_case = int(input())


def pascal(lst, idx):
    if idx == 0:
        return
    print(' '.join(map(str, lst)))
    start = 0
    last = len(lst) - 1
    result = []
    prev = -1
    for i in range(len(lst)):
        if i == start:
            result += [lst[i]]

        if prev >= 0:
            result += [lst[prev] + lst[i]]
            prev = i
        else:
            prev = 0
        if i == last:
            result += [lst[i]]
    # print(' '.join(result))
    pascal(result, idx - 1)


for num in range(test_case):
    idx = int(input())
    print(f'#{num + 1}')
    pascal([1], idx)







