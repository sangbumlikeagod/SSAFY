import sys
# print(__name__)
file = open('poppop.txt', 'r')
sys.stdin = file

test_case = int(input())



def sumofiter( idxx, idxy):
    result = 0
    # map( lambda x: result + x , [ iter[idxx + x[0]][idxy + x[1]] for x in [[0, 0], [0,1], [0, -1], [1, 0], [-1, 0]]  if 0 <= idxx +  x[0]< N if 0 <= idxy +  x[1] < M])
    for i in  [ iter[idxx + x[0]][idxy + x[1]] for x in [[0, 0], [0,1], [0, -1], [1, 0], [-1, 0]]  if 0 <= idxx +  x[0]< N if 0 <= idxy +  x[1] < M]:
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