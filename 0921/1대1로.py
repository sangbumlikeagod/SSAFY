import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

def find_pa(node):
    if sett[node] == node:
        return node
    sett[node] = find_pa(sett[node])
    return sett[node]

def union(node1, node2):
    tmp1 = find_pa(node1)
    tmp2 = find_pa(node2)
    if tmp1 > tmp2:
        sett[tmp1] = tmp2
    else:
        sett[tmp2] = tmp1 

import heapq
for num in range(test_case):
    return_value = 0
    N = int(input())
    sett = [i for i in range(N)]
    lstq = []
    x_l = list(map(int, input().split()))
    y_l = list(map(int, input().split()))
    for i in range(N):
        for j in range(i + 1, N):
            heapq.heappush(lstq, ( ((x_l[i] - x_l[j]) ** 2 + (y_l[i] - y_l[j]) ** 2 ) , i, j))
    e = float(input())


    val = 0
    while val < N - 1:
        while find_pa(lstq[0][1]) == find_pa(lstq[0][2]):
            heapq.heappop(lstq)
        v, a1, a2 = heapq.heappop(lstq)

        return_value += v
        union(a1, a2)
        val += 1



    print(f'#{num + 1} {round(return_value * e)}')