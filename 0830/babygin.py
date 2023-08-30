import sys

name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file


test_case = int(input())


def is_baby(num, dic):
    if num - 1 in dic and num + 1 in dic:
        new_dic = dic.copy()
        new_dic[num] -= 1
        if new_dic[num] == 0:
            new_dic.pop(num)

        new_dic[num - 1] -= 1
        if new_dic[num - 1] == 0:
            new_dic.pop(num - 1)

        new_dic[num + 1] -= 1
        if new_dic[num + 1] == 0:
            new_dic.pop(num + 1)

    elif num - 1 in dic and num - 2 in dic:
        new_dic = dic.copy()
        new_dic[num] -= 1
        if new_dic[num] == 0:
            new_dic.pop(num)

        new_dic[num - 1] -= 1
        if new_dic[num - 1] == 0:
            new_dic.pop(num - 1)

        new_dic[num - 2] -= 1
        if new_dic[num - 2] == 0:
            new_dic.pop(num - 2)

    elif num +1 in dic and num + 2 in dic:
        new_dic = dic.copy()
        new_dic[num] -= 1
        if new_dic[num] == 0:
            new_dic.pop(num)

        new_dic[num + 2] -= 1
        if new_dic[num + 2] == 0:
            new_dic.pop(num + 2)

        new_dic[num + 1] -= 1
        if new_dic[num + 1] == 0:
            new_dic.pop(num + 1)
    else:
        return 0
    return is_baby_gin(new_dic)


def is_gin(num, dic):
    if dic[num] >= 3:
        new_dic = dic.copy()
        new_dic[num] -= 3
        if new_dic[num] == 0:
            new_dic.pop(num)
    else:
        return 0
    return is_baby_gin(new_dic)


def is_baby_gin(dic):
    # print(dic)
    if not dic:
        return 1
    
    for i in dic:
        if is_baby(i, dic) or is_gin(i, dic):
            return 1

    return 0


for num in range(test_case):
    dic = {}
    for inte in input().strip():
        dic[int(inte)] = dic.get(int(inte), 0) + 1

    print(f'#{num + 1} {is_baby_gin(dic)}')
 

