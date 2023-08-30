
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


    def change(self, idx):
        if self.heap[idx] < self.heap[idx // 2]:
            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            self.change(idx // 2)

    def sum_with_ancestor(self, idx):
        if idx == 1:
            return self.heap[idx]
        else:
            return self.heap[idx] + self.sum_with_ancestor(idx // 2)

for num in range(test_case):

    lst = Listheap(int(input()))
    for i in list(map(int, input().split())):
        lst.enqueue(i)

    print(f'#{num + 1} {lst.sum_with_ancestor(lst.end) - lst.heap[lst.end]}')