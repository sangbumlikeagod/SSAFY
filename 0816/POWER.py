# 거듭제곱의 문제

def f1(b, e):
    ans = 1
    for _ in range(e):
        ans *= b
    return ans


def f2(b, e):
    if b == 0 or e == 0:
        return 1
    if e % 2:
        r = f2(b, (e-1) // 2)
        return r * r * b
    else:
        r = f2(b, e//2)
        return r * r


print(f2(2, 10))
print(f1(2, 10))
# mergesort처럼 분할하고 정복한다는 뜻인듯 퀵정렬 역시 분할 정복을 사용한다. 이미 알고있긴 했음
