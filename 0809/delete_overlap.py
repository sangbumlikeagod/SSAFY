import sys

file = open('delete_overlap.txt', 'r')
sys.stdin = file

test_case = int(input())


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
                return len(lst_num)
            else:
                continue

    return 0


for num in range(test_case):
    print(f'#{num + 1} {search(list(input()))}')