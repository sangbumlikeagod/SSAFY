import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
test_case = 10


for num in range(test_case):
    return_value = 0
    # 델타로 할건데
    # 범위 설정 먼저
    N, M = map(int, input().split())
    # can_go = [[i, j] for i in range(-M + 1, M) for j in range(-M + 1, M) if abs(i) + abs(j) < M]
    # print(can_go)
    # 수익을 유지하면서, 가장 많은집에 줄 수 있는 케이스
    # break
    lst = []
    house = 0
    for _ in range(N):
        row = list(map(int, input().split()))
        house += row.count(1)
        lst.append(row)
    # print(house)
    # print(lst)
    maximum = 0
    while maximum ** 2 + (maximum - 1) ** 2 <= house * M:
        maximum += 1
    # print(maximum)

    while maximum > 0:
        budget = maximum ** 2 + (maximum - 1) ** 2
        # 일단 최대일때가 반드시 최대 답일 수밖에 없음
        # 덮어 버리니까 그래서 전부 돌건데 작아질 경우는 하나로 만약에 한번도 운용 금액을 넘지 못하면 작아짐
        local = 0
        for row in range(N):
            for column in range(N):

                can_go = [lst[row + i][column + j] * M for i in range(-maximum + 1, maximum) for j in range(-maximum + 1, maximum)\
                          if abs(i) + abs(j) < maximum\
                          if 0 <= row + i < N\
                          if 0 <= column + j < N
                          ]
                # print(sum(can_go))
                if sum(can_go) >= budget and sum(can_go) > local:
                    local = sum(can_go)

        if local == 0:
            maximum -= 1
            continue
        else:
            return_value = local // M
            break

    print(f'#{num + 1} {return_value}')
