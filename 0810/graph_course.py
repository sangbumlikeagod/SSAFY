import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


def search(start, end):
    dic_occupied[start] = 1
    if start in dic:
        for i in dic[start]:
            if not dic_occupied[i]:
                if i == end:
                    return 1
                if search(i, end):
                    return 1
    return 0

for num in range(test_case):
    V, E = map(int, input().split())
    dic = {}
    dic_occupied = {}
    for i in range(E):
        s, e = input().split()
        dic[s] = dic.get(s, []) + [e]
        dic_occupied[s] = 0
        dic_occupied[e] = 0
    S, G = input().split()

    print(f'#{num + 1} {search(S, G)}')