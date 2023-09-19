import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


def merge_sort(lst):   
    global right
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            right += 1
            lst[0], lst[1] = lst[1], lst[0]
        return lst
    A = merge_sort(lst[:len(lst) // 2])
    B = merge_sort(lst[len(lst) // 2:])

    if A[-1] > B[-1]:
        right += 1

    # print(A, B)
    nlst = []
    a = b = 0
    while a != -1 or b != -1 :
        # print(a, b, A, B)
        # print('\t', nlst)
        if a == -1:
            nlst.append(B[b])
            # print('\t',B[b])
            b = b + 1 if b + 1 < len(B) else -1
        elif b == -1:
            # print('\t',A[a])
            nlst.append(A[a])
            a = a + 1 if a + 1 < len(A) else -1
        else:
            if A[a] < B[b]:
                # print('\t',A[a])
                nlst.append(A[a])
                a = a + 1 if a + 1 < len(A) else -1
            elif A[a] > B[b]:
                nlst.append(B[b])
                # print('\t',B[b])
                b = b + 1 if b + 1 < len(B) else -1
            else:
                nlst.append(A[a])
                nlst.append(B[b])
                # print('\t',A[a])
                # print('\t',B[b])
                a = a + 1 if a + 1 < len(A) else -1
                b = b + 1 if b + 1< len(B) else -1
    # if a < b:
    #     nlst.append(a)
    #     if b != -1:
    #         nlst.append(b)
    # elif b < a:
    #     nlst.append(b)
    #     if a != -1:
    #         nlst.append(a)
    # print(nlst)
    return nlst


        
for num in range(test_case):
    left = right = 0
    return_value = 0
    N = int(input())
    lst = list(map(int, input().split()))
    # print(lst)



    print(f'#{num + 1} {merge_sort(lst)[N // 2]} {right}')