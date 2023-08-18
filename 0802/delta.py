import sys

file = open('delta.txt', 'r')
sys.stdin = file

test_case = int(input())


def sum(node, arr):
    ans = 0

    for i in arr:
        if i > node:
            ans += i - node
        else:
            ans += node - i

    return ans


for num in range(test_case):

    size = int(input())
    table = [list(map(int, input().split())) for _ in range(size)]
    return_value = 0
    for i in range(size):
        for j in range(size):
            return_value += sum(table[i][j], [table[i + _[0]][j + _[1]] for _ in [[0, 1], [0, -1], [1, 0], [-1, 0]] if 0 <= i + _[0] < size if 0 <= j + _[1] < size])

    print(f'#{num + 1} {return_value}')