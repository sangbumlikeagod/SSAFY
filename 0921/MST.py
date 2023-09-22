
import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
import heapq


class Tree:
    def __init__(self, hq) -> None:
        self.hq = hq
        self.set = [i for i in range(V + 1)]
        self.set_len = 0
    
    def find_pa(self, node):
        if self.set[node] == node:
            return node
        self.set[node] = self.find_pa(self.set[node])
        return self.set[node]

    def union(self, node1, node2):
        tmp1 = self.find_pa(node1)
        tmp2 = self.find_pa(node2)
        if tmp1 > tmp2:
            self.set[tmp1] = tmp2
        else:
            self.set[tmp2] = tmp1 


    def mst(self):
        val = 0
        while self.set_len < V:
            
            while self.find_pa(self.hq[0][1]) == self.find_pa(self.hq[0][2]):
                heapq.heappop(self.hq)
            v, a1, a2 = heapq.heappop(self.hq)
            # print(v, a1, a2, self.hq)
            val += v
            self.union(a1, a2)
            # print(self.set)
            self.set_len += 1
            # print(self.hq, self.set, self.set_len)
        return val
# v가 너무 커서 안될것같음 
# 싸이클이라는걸 알아차리기 위해서는 더한 준비가 필요하다 
# 리스트 부모형태로 해서 구하면 어떄 
for num in range(test_case):
    return_value = 0
    V, E = map(int, input().split())
    # in_lst = [[0] * E for _ in range(V + 1)]
    t = Tree([])
    for i in range(E):
        v, e, val = map(int, input().split())
        if e < v:
            v, e = e, v
        heapq.heappush(t.hq, (val, v, e))
    # t.set[t.hq[0][2]] = t.hq[0][1]  
    # print(t.hq, t.set, t.set_len)

    print(f'#{num + 1} {t.mst()}')