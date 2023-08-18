class LinearQ:
    def __init__(self, limit):
        self.queue = {}
        self.front = -1
        self.rear = 0
        self.size = limit

    def enqueue(self, content):
        self.queue[self.rear] = content
        self.rear += 1

    def dequeue(self):
        if self.full():
            print(' 꽉 참 ')
            return
        self.front += 1
        return  self.queue[self.front]

    def full(self):
        return self.rear - self.front == self.size

    def isempty(self):
        return self.front == self.rear

    def Qpeek(self):
        if self.front == -1:
            return
        return self.queue[self.front]

# 연결리스트 큐를 쓰는 경우도 있고 선형 큐를 쓰는 경우도 있고 원형 큐를 쓰는 경우도 있다

a = LinearQ(3)

a.enqueue(3)
a.Qpeek()

class CircularQ:
    def __init__(self, limit):
        self.queue = {}
        self.front = -1
        self.rear = 0
        self.size = limit

    def enqueue(self, content):
        if self.full():
            print(' 꽉 참 ')
            return
        self.queue[self.rear] = content
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        self.front += (self.front + 1) % self.size
        if self.isempty():
            print(' 텅 빔 ')
            return
        return self.queue[self.front]

    def isempty(self):
        return self.front == self.rear and not self.queue[self.front]

    def full(self):
        # return self.front == self.rear and self.queue[self.front]
        return (self.front == (self.rear + 1) // self.size) or (self.front == -1 and self.rear == self.size - 1)
    # full 에 조금 어려움이 있음
    def Qpeek(self):
        if self.front == -1:
            return
        return self.queue[self.front]


b = CircularQ(5)
b.enqueue(1)
b.enqueue(2)
b.enqueue(3)
b.enqueue(4)
b.enqueue(5)

k = b.isempty()
k2 = b.full()
# b.enqueue(5)
print('끝')