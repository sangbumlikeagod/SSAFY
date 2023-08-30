import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    return_value = 0
    # 400개의 있다. 서로 안겹치게
    student = int(input())
    room = [0] * 401

    for i in range(student):
        start, end = map(int, input().split())
        if end < start:
            end, start = start, end
        if not start % 2:
            start -= 1
        if end % 2:
            end += 1
        print(start,end)
        for k in range(start, end + 1):
            room[k] += 1
            if room[k] > return_value:
                return_value = room[k]
    print(room)

    print(f'#{num + 1} {return_value}')