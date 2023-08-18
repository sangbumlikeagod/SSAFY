import sys
file = open('1945.txt', 'r', encoding='utf-8')
sys.stdin = file

test_case = int(input())


def divide_prime(given, prime):
    if given % prime != 0:
        return 0
    else:
        return divide_prime(given // prime, prime) + 1


for num in range(test_case):
    given_num = int(input())
    ans = []
    prime_lst = [2, 3, 5, 7, 11]
    for prime in prime_lst:
        ans.append(divide_prime(given_num, prime))
    print(f'#{num + 1} {" ".join(map(str, ans))}')





