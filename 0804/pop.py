import sys
# print(__name__)
file = open('pop.txt', 'r')
sys.stdin = file

test_case = int(input())




def sumofiter( idxx, idxy):
    result = 0
    x_range = [[k, 0] for k in range(-iter[idxx][idxy], iter[idxx][idxy] + 1)]
    y_range = [[0, k] for k in range(-iter[idxx][idxy], iter[idxx][idxy] + 1)]
    rannnge = x_range + y_range

    # if rannnge:
    rannnge.remove(([0, 0]))
    # print(rannnge)
    # map( lambda x: result + x , [ iter[idxx + x[0]][idxy + x[1]] for x in [[0, 0], [0,1], [0, -1], [1, 0], [-1, 0]]  if 0 <= idxx +  x[0]< N if 0 <= idxy +  x[1] < M])
    for i in [iter[idxx + x[0]][idxy + x[1]] for x in rannnge if 0 <= idxx + x[0] < N if 0 <= idxy + x[1] < M]:
        result += i
    return result


for num in range(test_case):
    N, M = map(int, input().split())

    iter = [list(map(int, input().split())) for _ in range(N)]

    max_flower = 0
    for i in range(N):
        for j in range(M):
            localss = sumofiter(i, j)
            if localss > max_flower:
                max_flower = localss





    print(f'#{num + 1} {max_flower}')