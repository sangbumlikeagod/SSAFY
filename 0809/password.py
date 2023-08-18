import sys

file = open('password.txt', 'r')
sys.stdin = file

test_case = 10


def search(lst_num):
    while lst_num:
        size = len(lst_num)
        i = 0
        while i < size - 1:

            if lst_num[i] == lst_num[i + 1]:
                lst_num.pop(i + 1)
                lst_num.pop(i)
                break
            i += 1

        else:
            if size == len(lst_num):
                return lst_num
            else:
                continue

    return ''


for num in range(test_case):
    N, M = input().split()
    N = int(N)
    M = list(M)

    print(f'#{num + 1} {"".join(search(M))}')