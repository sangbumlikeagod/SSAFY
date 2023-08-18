import sys

file = open('palindrome.txt', 'r')
sys.stdin = file
test_case = 10

for num in range(test_case):
    case = int(input())
    lst = [input() for _ in range(8)]
    count = 0
    for column in range(8):
        for row in range(8):
            if column < 8 - case + 1:
                    # row case
                l, r = column, column + case - 1
                while l < r:
                    if lst[row][l] != lst[row][r]:
                        break
                    l += 1
                    r -= 1
                else:
                    if l >= r:
                        count += 1
            if row < 8 - case + 1:
                t, b = row, row + case - 1
                while t < b:
                    if lst[t][column] != lst[b][column]:
                        break
                    t += 1
                    b -= 1
                else:
                    if t >= b:
                        count += 1

    print(f'#{num + 1} {count}')