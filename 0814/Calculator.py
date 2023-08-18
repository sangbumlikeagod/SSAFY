import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10

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
    ')': 3
}


def classify(string):
    stack_non_digit = []
    stack_digit = []
    i = 0
    while i < size:

        while i < size and dic_icp.get(string[i], -1) == -1:
            stack_digit.append(int(string[i]))
            i += 1
        if not stack_non_digit:
            stack_non_digit.append(string[i])
        else:
            tmp = []
            while i < size and dic_isp.get(stack_non_digit[-1]) < dic_icp.get(string[i]):
                tmp.append(stack_non_digit.pop())
            else:
                if tmp:
                    stack_digit += [string[i]] + tmp
                else:
                    if i < size:
                        stack_non_digit.append(string[i])
        i += 1
    stack_digit += stack_non_digit
    return stack_digit


def calculate(stack):
    stack1 = []
    i = 0
    while i < size:
        if dic_icp.get(stack[i], -1) == -1:
            stack1.append(stack[i])
        else:
            num1, num2 = stack1.pop(), stack1.pop()
            if stack[i] == '+':
                stack1.append(num1 + num2)
            elif stack[i] == '-':
                stack1.append(num1 - num2)
        i += 1
    return stack1[0]


for num in range(test_case):
    return_value = 0
    size = int(input())
    print(f'#{num + 1} {calculate(classify(input()))}')