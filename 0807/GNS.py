import sys

file = open('GNS.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    dic = {}
    size = int(input().split()[1])
    lst = input().split()
    for i in lst:
        dic[i] = dic.get(i, 0) + 1
    return_value = 'ZRO ' * dic.get('ZRO', 0) +\
                    'ONE ' * dic.get('ONE', 0) +\
                    'TWO ' * dic.get('TWO', 0) +\
                    'THR ' * dic.get('THR', 0) +\
                    'FOR ' * dic.get('FOR', 0) +\
                    'FIV ' * dic.get('FIV', 0) +\
                    'SIX ' * dic.get('SIX', 0) +\
                    'SVN ' * dic.get('SVN', 0) +\
                    'EGT ' * dic.get('EGT', 0) +\
                    'NIN ' * dic.get('NIN', 0)
    print(f'#{num + 1} {return_value}')