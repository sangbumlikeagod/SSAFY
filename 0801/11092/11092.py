import sys
f = open('11092.txt', 'r', encoding='utf-8')
sys.stdin = f

case = int(input())

for i in range(case):
    count_int = int(input())
    int_list = list(map(int, input().split()))

    local_min = 0
    local_max = 0
    for idx in range(len(int_list)):
        if int_list[idx] < int_list[local_min]:
            local_min = idx
        if int_list[idx] >= int_list[local_max]:
            local_max = idx

    print(f'#{i+1} {abs(local_max - local_min)}')
