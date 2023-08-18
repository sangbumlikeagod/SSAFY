import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

def dynamic(integer):
    if integer == 10:
        return 1
    if integer == 0:
        return 1
    return 2 * dynamic(integer - 20) + dynamic(integer - 10)

for num in range(test_case):
    print(f'#{num + 1} {dynamic(int(input()))}')