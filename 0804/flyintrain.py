import sys

file = open('flyintrain.txt', 'r')
sys.stdin = file

test_case = int(input())


# ST_1로 가고 st_2에서 출발
def fly_die(s_f, s_t1, s_t2, dis):
    if dis < 10 ** -8:
        return dis / (s_f + s_t1) * s_f
    else:
        time = round(dis / (s_f + s_t1), 5)
        return time * s_f + fly_die(s_f, s_t2, s_t1, dis - (s_t1 + s_t2) * time)


for num in range(test_case):
    A, B, C, D = map(int, input().split())

    # 1번 움직일 때마다 3개가 동시에 움직임
    '''
    파리가 돌아다닐떄 다음에 도착하는데 걸리는 시간 = 파리와 그 놈 사이의 거리 / 둘의 속력의 합
    파리의 속도가 다른 기차보다 크기때문에 치여 죽을리는 없음 죽음은 두 기차 사이의 거리에만 의지함
    
    파리가 닿았을때 걸리는 시간 에서 두 차의 상대속력 만큼 거리는 짧아져 있음
    '''

    print(f'#{num + 1} {fly_die(D, B, C, A)}')