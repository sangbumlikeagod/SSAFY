import sys

file = open('comparison.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    word1 = input()
    word2 = input()
    size1 = len(word1)
    size2 = len(word2)
    return_value = 2
    i = 0
    while i < size2 - size1:

        if word1[0] == word2[i]:
            idx = 1
            j = i + 1
            while idx < size1:
                if word1[idx] == word2[j]:
                    idx += 1
                    j += 1
                else:
                    break
            if idx == size1:
                return_value = 1
                break
            i += 1
        else:
            i += 1
    return_value = 0 if return_value != 1 else 1


    print(f'#{num + 1} {return_value}')