import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file

test_case = int(input())

dic = {
    1 : [[1, 0], [0, 1], [0, -1], [-1, 0]],
    2 : [[1, 0], [-1, 0]],
    3 : [[0, -1], [0, 1]],
    4 : [[-1, 0], [0, 1]],
    5 : [[1, 0], [0, 1]],
    6 : [[1, 0], [0, -1]],
    7 : [[-1, 0], [0, -1]],

}

for num in range(test_case):
    return_value = 0
    queue_idx = 0 
    N, M, R, C, L = map(int,input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [ [0] * M for _ in range(N) ]
    visited[R][C] = 1
    queue = [((R, C), 1)]


    while queue_idx < len(queue):
        idx, hour = queue[queue_idx]
        if hour == L:
            break
        

        for i in dic[lst[idx[0]][idx[1]]]:
            # print(i)
            # 둘이 연결돼 있어야만 가능 -> 딕셔너리에 이 값이 있는지를 확인할 거임
            if 0 <= idx[0] + i[0] < N and 0 <= idx[1] + i[1] < M and not visited[idx[0] + i[0]][idx[1] + i[1]]\
                    and lst[idx[0] + i[0]][idx[1] + i[1]]\
                  and [-i[0], -i[1]] in dic[lst[idx[0] + i[0]][idx[1] + i[1]]]:
                visited[idx[0] + i[0]][idx[1] + i[1]] = 1
                return_value += 1
                queue.append(((idx[0] + i[0], idx[1] + i[1]), hour + 1))
        queue_idx += 1


    print(f'#{num + 1} {return_value + 1}')