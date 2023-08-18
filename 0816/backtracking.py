
cnt = 0
def f(i, N, t, s):
    global cnt
    cnt += 1
    if s == t:
        return 1
    if i == N:
        return 0
    elif s > t:
        return 0
    else:
        return f(i + 1, N, t, s) or f(i + 1, N, t, s + A[i])

# 재귀를 해서 배열의 각 요소에 접근하는 방법에 대해서 말한다\




A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
# B = [0, 0, 0]

print(f(0, N, 1, 0), cnt)

# for i in range(sum(A) + 3):
#     print(f(0, N, i, 0))

# print(f(0, N, 1, 0))
# print(B)
A = [1, 2, 3]
# for i in range(1 << 3): # 일반적인 비트연산은 그냥 숫자 계산에 지나지 않음
#     lst = []
#     for j in range(3):
#         if 1 << j & i:
#             lst.append(A[j])
#     print(lst)



    # print(i)
# 숫자 자체가 and와 or 연산을 지원하는데 그 연산의 기반이 비트기반이라고 봐야하는 것 같다.

print(1 | 2)
# 두 비트중 큰놈을 구하는게 아니라 둘의 비트 모든 요소에 or을 박는 것
bit = [0]
#또는
def f(i, N):
    if i == N:

        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end = ' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return
# 이런 방식을 이용한다.


A = [1, 2, 3]

# 이건 주어진 요소들의 모든 행렬을 리턴하는 걸 말하는 것 같음 모든 것이 in - place로 일어나는게 좀 좋은 방식일 수도
A = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]

min_sofar = float('inf')
def permutation(row_now, row_end, column_now, column_end, s):
    global min_sofar
    if row_now == row_end or s >= min_sofar:
        print(s)
        return s
        # print(A)
    else:
        print(A, s + A[row_now][column_now])
        a1 = permutation(row_now + 1, row_end, column_now + 1, column_end, s + A[row_now][column_now])
        if a1 < min_sofar:
            min_sofar = a1
        a2 = a1 + 1
        for j in range(column_now + 1, column_end):
            for row in range(row_now, row_end):
                A[row][column_now], A[row][j] = A[row][j], A[row][column_now]
            # print(A, s + A[row_now][column_now])
            a2 = permutation(row_now + 1, row_end, column_now + 1, column_end, s + A[row_now][column_now])
            if a2 < min_sofar:
                min_sofar = a2
        return min(a1, a2)





# 모든 행들의 열위치를 다바꿔주면 여러 차례의 문제도 해결가능

permutation(0, 3, 0, 3, 0)
print(min_sofar)