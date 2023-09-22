import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = 10


for num in range(test_case):
    dic = {}
    alarm_dic = {}
    length, start =map(int, input().split())
    relat = list(map(int, input().split()))
    for i in range(length // 2):
        dic[relat[i * 2]] = dic.get(relat[i * 2], []) + [relat[i * 2+ 1]]
        alarm_dic[relat[i * 2 + 1]] = alarm_dic[relat[i * 2]] = True

    from collections import deque
    que = deque()
    que.append((start, 1))
    max_prev = 0
    state = 0
    alarm_dic[start] = False
    while que:
        # print(que)
        next, stage = que.popleft()
        if stage != state:
            state += 1
            max_prev = next
        else:
            max_prev = max(next, max_prev)
        if next in dic:
            for i in dic[next]:
                if alarm_dic[i]:
                    alarm_dic[i] = False
                    que.append((i, stage + 1))
    
    print(f'#{num + 1} {max_prev}')
    # break