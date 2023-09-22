import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
import heapq

for num in range(test_case):
    return_value = 0
    N, E = map(int, input().split())
    dic = {}
    for i in range(E):
        s, e, w = map(int, input().split())
        dic[s] = dic.get(s, []) + [(w, e)]
    
    hea = [(0, 0)]
    while hea:

        val, next = heapq.heappop(hea)
        if next == N:
            return_value = val
            break
        for i in dic[next]:
            heapq.heappush(hea, (val + i[0], i[1]))


    print(f'#{num + 1} {return_value}')