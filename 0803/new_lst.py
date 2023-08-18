import sys

file = open('new_lst.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    countt = int(input())
    lst = list(map(int, input().split()))
    size = len(lst)
    idx = 0
    while idx < countt:
        min_d = 100000000
        max_d = -10000000
        min_idx = 0
        max_idx = 0
        for i in range(idx, size):
            if lst[i] < min_d:
                min_d, min_idx = lst[i], i
            if lst[i] > max_d :
                max_d, max_idx = lst[i], i

        print(idx, idx + 1, min_idx, max_idx)
        # print(lst[max_idx], lst[min_idx])
        lst[idx], lst[max_idx] = lst[max_idx], lst[idx]
        # print(lst)
        lst[idx + 1], lst[min_idx] = lst[min_idx], lst[idx + 1]
        print(lst)
        idx += 2



    print(f'#{num + 1} {" ".join(map(str, lst))}')