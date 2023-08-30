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

    def sum_with_ancestor(self, idx):
        if idx == 1:
            return self.heap[idx]
        else:
            return self.heap[idx] + self.sum_with_ancestor(idx // 2)

lst = Listheap(6)
for i in list(map(int, '7 2 5 3 4 6'.split())):
    lst.enqueue(i)
print(lst.heap)
for _ in range(6):
    print(lst.pop())