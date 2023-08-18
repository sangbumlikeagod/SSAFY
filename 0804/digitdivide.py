import sys

file = open('digitdivide.txt', 'r')
sys.stdin = file

test_case = int(input())
prime_lst = [2, 3, 5, 7, 11]
for num in range(test_case):
    big_num = int(input())
    return_value = ''

    for i in prime_lst:
        count = 0
        while big_num >= i:
            if big_num % i == 0:
                big_num //= i
                count += 1
            else:
                break
        return_value += f'{count} '

    print(f'#{num + 1} {return_value}')