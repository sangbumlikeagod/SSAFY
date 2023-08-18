import sys


name = __file__.split('\\')[-1][:-5]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10
def classify(string):
    stack_non_digit = []
    stack_digit = []
    i = 0
    while i < size:

        while i < size and string[i] != '+':
            stack_digit.append(int(string[i]))
            i += 1
        if not stack_non_digit:
            stack_non_digit.append(string[i])
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
        if stack[i] != '+':
            stack1.append(stack[i])
        else:
            num1, num2 = stack1.pop(), stack1.pop()
            if stack[i] == '+':
                stack1.append(num1 + num2)
        i += 1
    return stack1[0]


out_file = open(f'{name}-out.txt', 'r')
for num in range(test_case):
    size = int(input())
    ans = calculate(classify(input()))
    if int(out_file.readline().split()[1]) == ans:
        print('맞았습니다.')
    else:
        print('틀렸습니다.')
    print(f'#{num + 1} {ans}')