import sys

file = open('fishmoon.txt', 'r')
sys.stdin = file

test_case = int(input())

for num in range(test_case):
    N, M = map(int, input().split())
    string = ''
    for _ in range(N):
        string += input()
    # print(string)
    # 처음과 끝을 설정해주는 함수는
    '''
    
    둘의 이동거리의 합을  N - M으로만 맞춰주면됨 
    리스트 없이 할려니까 골떄리네 
    
    '''
    # i번 쨰에 대해서 처음과 끝을 설정 =< 처음과 끝의 순서가 뒤바뀌지 않을때 까지
    # 문자열[행 = i * 10 + j ]
    move_range = [[i, j] for i in range(N - M + 1) for j in range(N - M + 1) if i + j == N - M]


    # print(move_range)
    result = 0
    for row in range(N):

        for i, j in move_range:
            start = i
            end = N - 1 - j
            while start < end:
                if string[row * N + start] == string[row * N + end]:
                    start += 1
                    end -= 1
                else:
                    break
            # print(start, end)
            if start >= end:
                # string[start] ~ [end]다 가져와
                # print('우웩')
                result = string[row * N + i: row * N + N - 1 - j + 1]
        for i, j in move_range:
            start = i
            end = N - 1 - j
            while start < end:
                if string[start * N + row] == string[end * N + row]:
                    start += 1
                    end -= 1

                else:
                    break
            if start >= end:
                tmp = ''
                # print('우웩')
                for row_2 in range(i, N - 1 - j + 1):
                    tmp += string[row_2 * N + row]

                result = tmp



    print(f'#{num + 1} {result}')