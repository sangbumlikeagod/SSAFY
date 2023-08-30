import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

# out = open('output.txt','r')
for num in range(test_case):
    return_value = 'Possible'
    N, M, K = map(int, input().split())
    table = [0] * (11111 // M + 1)
    lst = list(map(int, input().split()))
    for i in lst:
        table[i // M] += 1
    # if num == 29:
    #     print(table)

    for i in range(len(table)):
        if table[i] > i * K:
            return_value = 'Impossible'
            break
        if i < len(table) - 1:
            table[i + 1] += table[i]

    # tmp = out.readline()
    # if tmp.split()[1] != return_value:
    #     # f'#{num + 1} {return_value}':
    #     print(str(tmp), f'#{num + 1} {return_value}', sep= '\n' )
    #     print(table)
    #     print(N, M, K)
    print(f'#{num + 1} {return_value}')