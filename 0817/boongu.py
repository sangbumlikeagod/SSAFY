import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
# test_case = 2
out_file = open(f'{name}-out.txt', 'r')

for num in range(test_case):
    return_value = 'Impossible'
    N, M, K = map(int,input().split())
    people = list(map(int, input().split()))
    M_stack = M
    pan_stack = 0
    people.sort()
    # print(people)

    for i in people:
        # print( pan_stack)
        if not pan_stack and i < M_stack:
            break
        elif pan_stack:
            pan_stack -= 1
            continue
        else:
            M_stack += M
            pan_stack += K - 1

    else:
        return_value = 'Possible'

    if out_file.readline().split()[1] == return_value:
        print('맞았습니다.')
    else:
        print('틀렸습니다.')
    print(f'#{num + 1} {return_value}')
