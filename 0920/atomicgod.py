import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    return_value = 0
    N = int(input())
    prev = {}
    from collections import deque
    que = deque()
    cord_table = {}
    for _ in range(N):
        x, y, di, energy = map(int, input().strip().split())
        cord_table[(2 * x, 2 * y)] = [(di, energy)]

    for __ in range(4000):
        overlap_alarm = {}
        new_table = {}
        for arg in cord_table:
            di, energy = cord_table[arg][0]
            if di == 1:
                if abs(arg[1] - 1) <= 2000:
                    if new_table.get((arg[0], arg[1] - 1), 0):
                        overlap_alarm[(arg[0], arg[1] - 1)] = overlap_alarm.get((arg[0], arg[1] - 1), new_table[(arg[0], arg[1] - 1)][0][1]) + energy

                    new_table[(arg[0], arg[1] - 1)] = new_table.get((arg[0], arg[1] - 1), []) + [(di, energy)]
            elif di == 0:
                if abs(arg[1] + 1) <= 2000:
                    if new_table.get((arg[0], arg[1] + 1), 0):
                        overlap_alarm[(arg[0], arg[1] + 1)] = overlap_alarm.get((arg[0], arg[1] + 1), new_table[(arg[0], arg[1] + 1)][0][1]) + energy

                    new_table[(arg[0], arg[1] + 1)] = new_table.get((arg[0], arg[1] + 1), []) + [(di, energy)]
            elif di == 2:
                if abs(arg[0] - 1) <= 2000:
                    if new_table.get((arg[0] - 1, arg[1]), 0):
                        overlap_alarm[(arg[0] - 1, arg[1])] = overlap_alarm.get((arg[0] - 1, arg[1]), new_table[(arg[0] - 1, arg[1])][0][1]) + energy

                    new_table[(arg[0] - 1, arg[1])] = new_table.get((arg[0] - 1, arg[1]), []) + [(di, energy)]
            else:
                if abs(arg[0] + 1) <= 2000:
                    if new_table.get((arg[0] + 1, arg[1]), 0):
                        overlap_alarm[(arg[0] + 1, arg[1])] = overlap_alarm.get((arg[0] + 1, arg[1]), new_table[(arg[0] + 1, arg[1])][0][1]) + energy

                    new_table[(arg[0] + 1, arg[1])] = new_table.get((arg[0] + 1, arg[1]), []) + [(di, energy)]
        for i in overlap_alarm:
            return_value += overlap_alarm[i]
            new_table.pop(i)
        cord_table = new_table
        if not cord_table:
            break
    print(f'#{num + 1} {return_value}')
    # break