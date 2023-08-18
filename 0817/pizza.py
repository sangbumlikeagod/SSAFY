import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
# test_case =1


class CircularQ:
    def __init__(self, limit):
        self.queue = [0] * (limit + 1)
        self.front = 0
        self.rear = 0
        self.size = limit + 1

    def enqueue(self, content):
        # if self.full():
        #     print(' 꽉 참 ')
        #     return
        # 겹치는 걸 허용하지 않을 경우

        if self.full():
            self.rear = (self.rear + 1) % self.size
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = content

        # if self.rear == self.front:
        #     self.front = (self.front + 1) % self.size

    def dequeue(self):
        if self.isempty():
            print(' 텅 빔 ')
            return

        self.front = (self.front + 1) % self.size
        value = self.queue[self.front]
        self.queue[self.front] = 0
        return value

    def isempty(self):
        return self.front == self.rear

    def full(self):
        return (self.rear + 1) % self.size == self.front

    def Qpeek(self):
        if self.isempty():
            return '실패'
        return self.queue[(self.front + 1) % self.size]


for num in range(test_case):
    return_value = 0
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    que = CircularQ(N)
    # N개를 순서대로 넣을 것
    i = 0
    while i < N:
        que.enqueue([i + 1, lst[i]])
        i += 1
    a = 0

    while not que.isempty():
        print(que.queue, que.front, que.rear, que.Qpeek())
        a = que.dequeue()
        a[1] //= 2
        # print(a)
        if a[1] == 0:
            print('\t sex')
            if i < len(lst):
                que.enqueue([i + 1, lst[i]])
                i += 1
                # print(que.queue)
        else:
            print('sex')
            que.enqueue(a)
    # print(que.queue,que.front, que.rear)
    print(f'#{num + 1} {a}')

# que = CircularQ(6)
# for i in range(1, 10):
#     que.enqueue(i)
#     print(que.queue, que.isempty(), que.full())
# for _ in range(10):
#     print(que.dequeue())
#     print(que.Qpeek())
#     print(que.queue, que.isempty(), que.full())

# full을 적용 하면 이렇게되는데