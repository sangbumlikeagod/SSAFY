import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10

class Listheap:
    def __init__(self, size):
        self.end = 0
        self.heap = [0] * (size + 1)
        self.dic = {'*' : True,
                    '+' : True,
                    '-' : True,
                    '/' : True}

    def calculate(self, idx):
        # print(idx, self.heap[idx], len(self.heap))
        if self.heap[idx] not in self.dic:
            return self.heap[idx]
        else:
            if table[idx]:
                i = table[idx]
                i[0], i[1] = int(i[0]), int(i[1])

                if self.heap[idx] == '*':
                    return self.calculate(i[0]) * self.calculate(i[1])
                if self.heap[idx] == '/':
                    return int(self.calculate(i[0]) / self.calculate(i[1]))
                if self.heap[idx] == '+':
                    return self.calculate(i[0]) + self.calculate(i[1])
                if self.heap[idx] == '-':
                    return self.calculate(i[0]) - self.calculate(i[1])



for num in range(test_case):
    node = int(input())
    lst = Listheap(node)
    table = {}
    for _ in range(node):
        a, b, *c = input().split()
        # print(a, b, c)
        a = int(a)
        if b not in lst.dic:
            b = int(b)
        lst.heap[a] = b
        table[a] = table.get(a, []) + c
    # print(table)
    # print(lst.heap)
    print(f'#{num + 1} {lst.calculate(1)}')