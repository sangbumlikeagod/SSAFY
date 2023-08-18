import sys

file = open('count_char.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    word1 = input()
    word2 = input()
    wordset =set(word1)
    dic = {}
    for char in wordset:
        for small in word2:
            if small == char:
                dic[char] = dic.get(char, 0) + 1
    max_int = 0
    for i in dic:
        if dic[i] > max_int:
            max_int = dic[i]



    print(f'#{num + 1} {max_int}')