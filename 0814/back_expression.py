
import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 1

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
            while i < size and stack_non_digit and dic_isp.get(stack_non_digit[-1]) >= dic_icp.get(string[i]):
                tmp.append(stack_non_digit.pop())
            else:
                # print(tmp)
                if tmp:
                    stack_digit += tmp
                    stack_non_digit += [string[i]]
                else:
                    if i < size:
                        stack_non_digit.append(string[i])
        i += 1
    while stack_non_digit:
        stack_digit += stack_non_digit.pop()
    return ''.join(map(str, stack_digit))


for num in range(test_case):
    return_value = 0
    case = int(input())
    expression = input()

    size = len(expression)
    print(f'#{num + 1} {classify(expression)}')