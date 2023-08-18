
class stack:
    def __init__(self):
        self.stack = {}
        self.idx = -1

    def empty(self):
        return self.idx == -1

    def size(self):
        return self.idx + 1

    def __str__(self):
        if self.idx == -1:
            return '[ ]'
        else:
            return '[' + ', '.join(map(str, self.stack.values())) + ']'

    def pop(self):
        if self.idx == -1:
            print(' No index ')
            return None
        else:
            self.idx -= 1
            return self.stack.pop(self.idx)
    def push(self, k):
        self.idx += 1
        self.stack[self.idx] = k

    def __del__(self):
        pass


a = stack()

a.push(5)
a.push('5')
print(a)
print(a.pop(), a)
print(a.size())