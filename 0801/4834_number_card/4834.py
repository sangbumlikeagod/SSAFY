import sys
f = open('4834_input.txt', 'r', encoding='utf-8')
sys.stdin = f

test_case = int(input())
for num in range(test_case):
    card_num = int(input())
    card = int(input())
    dic = {}
    max_int = 0
    for _ in range(card_num):
        decimal = card % 10
        dic[decimal] = dic.get(decimal, 0) + 1
        if dic.get(max_int, 0) < dic.get(decimal):
            max_int = decimal
        elif dic.get(max_int, 0) == dic.get(decimal):
            if decimal > max_int:
                max_int = decimal
        card //= 10
    print(f'#{num + 1} {max_int} {dic[max_int]}')