

def ispartialsum(lst):
    count = len(lst)

    for i in range(1, 1 << count):
        ans = 0
        for j in range(count):
            if i & (1 << j):
                # print(lst[j])
                ans += lst[j]
        if ans == 0:
            return True

    return False

import sys

file = open('list_2.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):


    print(f'#{num + 1} {ispartialsum(list(map(int, input().split())))}')

