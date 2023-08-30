import sys

name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file

'''

최소인 차이값을 구하고 당근이 
한 상자에 N // 2를 초과하는 당근이 있어서도 안된다.
앞에서 부터 N // 3 개를 가져갈 수가 있다면 상관이 없으나 이제 문제라면 같은애들이 존재한다는 것.

그걸 고려해주려면 전부 다 받고 정렬을 해야겠는데. 
'''

harvest = int(input())

for i in range(harvest):

    carrot = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    stop = False
    new_lst = [0] * (lst[-1] + 1)
    for num in lst:
        new_lst[num] += 1
        if new_lst[num] > len(lst) // 2:

            stop = True
            break
    if new_lst.count(0) + 3 > len(new_lst):
        stop = True
    if stop:
        print(f'#{i + 1} -1')
        continue


    min_v = 1000
    for mid_start in range(2, len(new_lst) - 1):
        # print(mid_start)
        ans_front = 0
        break_law = False
        for front in range(1, mid_start):
            ans_front += new_lst[front]
            if ans_front > len(lst) // 2:
                break_law = True
                break

        # print(ans_front, end= ' ')
        if break_law:
            continue
        print(ans_front, end= '   ')
        for mid_end in range(mid_start, len(new_lst) - 1):
            break_law = False
            ans_mid = 0
            for mid in range(mid_start, mid_end + 1):
                ans_mid += new_lst[mid]
                # print(ans_mid)
                if ans_mid > len(lst) // 2:
                    break_law = True
                    break
            if break_law:
                # print(ans_mid)
                continue
            # print(ans_mid, end= ' ')
            ans_last = 0
            for last in range(mid_end + 1, len(new_lst)):
                ans_last += new_lst[last]
                if ans_last > len(lst) // 2:
                    break_law = True
                    break
            # print(mid_start, mid_end)
            if break_law:
                continue
            # print(ans_last)
            print(ans_front, ans_mid, ans_last)
            if max(ans_front, ans_mid, ans_last) - min(ans_front, ans_mid, ans_last) < min_v:
                # print(ans_front, ans_mid, ans_last)
                min_v = max(ans_front, ans_mid, ans_last) - min(ans_front, ans_mid, ans_last)

        # if break_law:
        #     continue

    print(f'#{i + 1} {min_v}')


        # 시작점을 잡았음
        # 끝점을 잡아

# 제발 좀 정상적으로 풀어
    # 지금 풀이에선 3개의 층으로 나누는 중
    # 난 리스트를 카운팅해서 하고싶은데