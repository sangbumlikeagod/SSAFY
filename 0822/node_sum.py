import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


class Listheap:
    def __init__(self, size):
        self.end = 0
        self.heap = [0] * (size + 1)

    def enqueue(self, content):
        self.end += 1
        self.heap[self.end] = content
        self.change(self.end)

    def pop(self):
        if self.end == 0:
            return 'x'
        return_value = self.heap[1]
        self.heap[self.end], self.heap[1] = 0,  self.heap[self.end]
        self.end -= 1
        self.rootchange(1)
        print(self.heap)
        return return_value


    def rootchange(self, idx):
        if self.end == 0:
            return 'x'
        if idx * 2 <= self.end:
            next = idx * 2
            if idx * 2 + 1 <= self.end:
                if self.heap[idx * 2 + 1] < self.heap[idx * 2]:
                    next = idx * 2 + 1
            if self.heap[next] < self.heap[idx]:
                self.heap[next], self.heap[idx] = self.heap[idx], self.heap[next]
                self.rootchange(next)

    def change(self, idx):
        if self.heap[idx] < self.heap[idx // 2]:
            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            self.change(idx // 2)

    def sum_of_ancestor(self, idx):
        ans = self.heap[idx]
        if idx * 2 <= self.end:
            ans += self.sum_of_ancestor(idx * 2)
            if idx * 2 + 1 <= self.end:
                ans += self.sum_of_ancestor(idx * 2 + 1)
        self.heap[idx] = ans
        return ans


for num in range(test_case):
    return_value = 0
    N, M, L = map(int, input().split())
    lst = Listheap(N)
    lst.end = N
    for i in range(M):
        where, val = map(int, input().split())
        lst.heap[where] = val


    print(f'#{num + 1} {lst.sum_of_ancestor(L)}')