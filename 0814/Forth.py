import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())



dic_isp = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,
}

dic_icp = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 3,
    ')': 3,
    '.': 0
}


def calculate(stack):
    stack1 = []
    i = 0
    while i < size:
        if dic_icp.get(stack[i], -1) == -1:
            stack1.append(int(stack[i]))
        elif stack[i] == '.':
            if len(stack1) != 1:
                return 'error'
            return stack1[0]
        else:
            if len(stack1) < 2:
                return 'error'
            num2, num1 = stack1.pop(), stack1.pop()
            if stack[i] == '+':
                stack1.append(num1 + num2)
            elif stack[i] == '-':
                stack1.append(num1 - num2)
            elif stack[i] == '*':
                stack1.append(num1 * num2)
            else:
                if num2 == 0:
                    return 'error'
                stack1.append(num1 // num2)
        i += 1


for num in range(test_case):
    lst = list(input().split())

    size = len(lst)
    print(f'#{num + 1} {calculate(lst)}')