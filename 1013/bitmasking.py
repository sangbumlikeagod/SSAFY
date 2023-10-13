a = [i for i in range(25)]
N = 25
cnt = 0
# 0 부터 2 ^ 25까지 ?
for i in range(1<<N):
    # 25개의 range에 대해서 
    for j in range(N):
        # j번째 자리수가 있다면 
        if i&(1<<j):
            # cnt에 1을 더한다
            cnt +=1
    # a의 길이가 25보다 길다거나 0이면 continue를 한다
    if len(a) > 5 or len(a) == 0:
        continue
    # 여기서부터 코드진행
print(cnt)