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
        # print(stack_non_digit , stack_digit, i)
        while i < size and dic_icp.get(string[i], -1) == -1:

            stack_digit.append(int(string[i]))
            i += 1
        if not stack_non_digit:
            stack_non_digit.append(string[i])
        else:
            # 근데 이게 아니었던 걸로 기억함 후위 표기식에서 변환할때 최고의 값은
            tmp = []
            while i < size and stack_non_digit and dic_isp.get(stack_non_digit[-1]) >= dic_icp.get(string[i]):
                # print(i)
                calcul = stack_non_digit.pop()
                if calcul != '(':
                    tmp.append(calcul)
            else:
                if tmp:
                    stack_digit += tmp
                    if string[i] != ')':
                        stack_non_digit.append(string[i])
                else:
                    if i < size:
                        if string[i] != ')':
                            stack_non_digit.append(string[i])
        i += 1
    stack_digit += [stack_non_digit[i] for i in range(len(stack_non_digit) -1 , -1, -1) if i != '(']
    return stack_digit


def calculate(stack):
    # print(stack)
    stack1 = []
    i = 0
    while i < len(stack):
        # print(stack1)
        if dic_icp.get(stack[i], -1) == -1:
            stack1.append(stack[i])
        else:
            if len(stack1) >= 2:
                num1, num2 = stack1.pop(), stack1.pop()
                if stack[i] == '+':
                    stack1.append(num2 + num1)
                elif stack[i] == '-':
                    stack1.append(num2 - num1)
                elif stack[i] == '/':
                    stack1.append(num2 / num1)
                elif stack[i] == '*':
                    stack1.append(num2 * num1)
        i += 1
    return stack1[0]


for num in range(test_case):
    return_value = 0
    size = int(input())
    print(f'#{num + 1} {calculate(classify(input()))}')