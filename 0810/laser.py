import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

#
# def search(idx, prev, state_steel):
#
#     if idx == len(arr):
#         return 0
#     add = 0
#     # print(num_of_steel, end = ' ')
#     if prev == '(' and arr[idx] != prev:
#         state_steel -= 1
#         add += state_steel
#
#
#     elif arr[idx] == '(':
#         state_steel += 1
#     else:
#         add += 1
#         state_steel -= 1
#
#     a = search(idx+1, arr[idx], state_steel) + add
#
#     return a


for num in range(test_case):
    num_of_steel = 0
    return_value = 0
    arr = input()
    size = len(arr)
    idx = 0
    prev = 0
    while idx < size:
        if prev == '(' and arr[idx] != prev:
            num_of_steel -= 1
            return_value += num_of_steel


        elif arr[idx] == '(':
            num_of_steel += 1
        else:
            return_value += 1
            num_of_steel -= 1
        idx, prev = idx + 1, arr[idx]

    print(f'#{num + 1} {return_value}')