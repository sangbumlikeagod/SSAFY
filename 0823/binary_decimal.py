import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())


for num in range(test_case):
    given = float(input())
    return_value = ''
    idx = 1
    for _ in range(13):
        # print(given, 1 / (1 << idx))
        if 1 / (1 << idx) <= given:
            given -= 1 / (1 << idx)
            return_value += '1'
        else:
            return_value += '0'
        idx += 1
        if given == 0: break
    else: return_value = 'overflow'

    print(f'#{num + 1} {return_value}')