import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    return_value = -1
    dic = {
        '}': 0,
        ']': 0,
        ')': 0,
        '{': '}',
        '[': ']',
        '(': ')'
    }
    string = input()
    for i in string:
        if i in dic:
            if type(dic[i]) == str:
                dic[dic[i]] += 1
            else:
                if dic[i]:
                    dic[i] -= 1
                else:
                    break
    else:
        if not dic['}'] + dic[')'] + dic[']']:
            return_value = 1

    print(f'#{num + 1} {return_value}')