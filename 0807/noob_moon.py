import sys

file = open('noob_moon.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    return_value = 2
    word = input()
    size = len(word)
    s = 0
    l = size - 1
    while s <= l:
        if word[s] == word[l]:
            s += 1
            l -= 1
            continue
        else:
            return_value = 0

            break

    return_value = 1 if return_value != 0 else 0
    print(f'#{num + 1} {return_value}')