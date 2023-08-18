import sys

file = open('fuckyou.txt', 'r')
sys.stdin = file

test_case = int(input())

def bruce(word1, word2):
    if len(word1) < len(word2):
        return len(word1)
    for i in range(len(word1) - len(word2) + 1):
        idx = 0
        while idx < len(word2):
            if word1[i + idx] != word2[idx]:
                break
            idx += 1
        else:
            if idx == len(word2):
                # print(word1[:i + idx] , word1[i + idx:])
                return bruce(word1[i + idx:], word2) + len(word1[:i]) + 1
    else:
        return len(word1)

for num in range(test_case):
    word1, word2 = input().split()
    print(f'#{num + 1} {bruce(word1, word2)}')