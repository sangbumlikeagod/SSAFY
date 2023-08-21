import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

# class Tree:
#     def __init__(self, node):
#         self.root = node
#     def put(self, node):
#         if node.val > self.root.val:
#             if self.root.right:
#
#             else:
#                 self.root, node.left = node, self.root
#
#
#
#
# class node:
#     def __init__(self, val):
#         node.val = val
#         node.left = None
#         node.right = None

for num in range(test_case):
    return_value = 0
    get = int(input())
    lst = [0] * (get + 1)
    index = 1

    def put(com):
        global index
        lst[index] = com
        if lst[index] > lst[index // 2]:








    print(f'#{num + 1} {return_value}')