import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
out_file = open(f'{name}-out.txt', 'r')

for num in range(test_case):
    return_value = 0




    if int(out_file.readline().split()[1]) == return_value:
        print('맞았습니다.')
    else:
        print('틀렸습니다.')
    print(f'#{num + 1} {return_value}')