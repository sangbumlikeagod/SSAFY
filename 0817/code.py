import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 1


class LinearQ:
    def __init__(self, limit):
        self.queue = {}
        self.front = -1
        self.rear = 0
        self.size = limit

    def enqueue(self, content):

        if self.full():
            print('꽉참')
            return
        self.queue[self.rear] = content
        self.rear += 1

    def dequeue(self):
        if self.isempty():
            print(' 텅 빔 ')
            return
        self.front += 1

        value = self.queue[self.front]
        self.queue.pop(self.front)
        return value

    def full(self):
        return self.rear - self.front - 1 == self.size

    def isempty(self):
        return self.front == self.rear

    def Qpeek(self):
        if self.front == -1:
            return
        return self.queue[self.front]


for num in range(test_case):
    num = int(input())
    return_value = 0
    lst = list(map(int, input().split()))
    q = LinearQ(8)

    for i in lst:
        q.enqueue(i)
    code = 1
    while True:

        a = q.dequeue()

        if a - code <= 0:
            q.enqueue(0)
            break

        q.enqueue(a - code)
        code = (code + 1) % 6 if not (code + 1) // 6 else 1
    # return_value = ''
    # for i in range(q.front + 1, q.rear):
    #     return_value += str(f'{q.queue[i]} ')
    return_value = ' '.join(map(str, [q.queue[i] for i in range(q.front + 1, q.rear)]))
    print(f'#{num} {return_value}')