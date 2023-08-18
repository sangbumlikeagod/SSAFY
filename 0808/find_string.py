import sys

file = open('find_string.txt', 'r', encoding='utf-8')
sys.stdin = file

test_case = 10
def bruce(word1, word2):
    count = 0
    for i in range(len(word1) - len(word2) + 1):
        idx = 0
        while idx < len(word2):
            if word1[i + idx] != word2[idx]:
                break
            idx += 1
        else:
            if idx == len(word2):
                count += 1
    return count

for num in range(test_case):
    what = int(input())
    word2 = input()
    word1 = input()

    print(f'#{num + 1} {bruce(word1, word2)}')