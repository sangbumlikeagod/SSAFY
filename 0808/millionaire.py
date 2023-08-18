import sys

file = open('millonaire.txt', 'r')
sys.stdin = file

test_case = int(input())


# for num in range(test_case):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     dic = {}
#     i = 0
#     total = 0
#     while i < N:
#         local = 0
#         keys = list(dic.keys())
#
#         for key in keys:
#             if key < lst[i]:
#                 total += (lst[i] - key) * dic[key]
#                 local += dic[key]
#                 dic.pop(key)
#         dic[lst[i]] = dic.get(lst[i], 0) + local + 1
#         last_buy = lst[i]
#         i += 1
#
#     print(f'#{num + 1} {total}')

test_case = 10
for num in range(test_case):
    N = int(input())
    lst = list(map(int, input().split()))
    size = len(lst)
    buy = sell = size - 1
    total = 0

    while buy >= 0:
        if lst[buy] > lst[sell]:
            sell = buy
            buy -= 1
            continue
        total += lst[sell] - lst[buy]
        buy -= 1

    # sell 을 마지막걸로 잡고 buy가 sell보다 크면 sell을 바꿔야한다
    print(f'#{num + 1} {total}')

    # 올라갈떄 사고 내려갈떄 파는건데 문제는 올라갈떄 뒤에 얼마나 더 큰 애들이 있을지 알 수가 없음 나중에가서 앞에애들 다 바꿔줘야 하는게 필연인데

