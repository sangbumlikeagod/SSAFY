import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
# test_case = 1

'''

반드시 n번을 바꿔야 하는 숫자가 있다.

가장 큰것을 가장 작은것과 바꾼다는게 가장 있어보이지만 
바뀌는 순서 역시도 중요하다

중복이 일어나는 일이 많을까? 모드에 따라 다르다. 애초에 큰수가 나와서 바꿀때마다
손해일 수도 있기 때문에 


어떤 수의 최대치를 알고 있어야만 가능하다.


'''

def characcharacchange(lst, left):
    # print(lst)
    global max_val

    if left == 0:
        local = 0
        for pow, num in enumerate(lst):
            local += num * 10 ** pow

        if max_val < local:
            max_val = local
        return 0
    min_value = 10000000
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j] , lst[i]
                # print(tmp)
                local = characcharacchange(lst, left - 1)
                lst[i], lst[j] = lst[j] , lst[i]
                if local < min_value:
                    min_value = local
    else:
        if min_value == 10000000: 
            local = 0
            for pow, num in enumerate(lst):
                    local += num * 10 ** pow
            if max_val < local:
                max_val = local
            return 0
        else: 
            return min_value + 1
        
for test in range(test_case):
    return_value = 0
    N, C = input().split()
    lst = list(map(int, list(N)))

    max_val = 0
    # 사실 이 문제는 N번 이상이면 무조건 자리를 찾아간다.
    if int(C) >= len(lst):
        howmany = characcharacchange(lst[::-1], len(lst))
    else:
        howmany = characcharacchange(lst[::-1], int(C))
    finish = False

    for i in range(9):
        if lst.count(i) > 1:
            print(f'#{test + 1} {max_val}')
            finish = True
            break
    if finish:
        continue
    if (int(C) - howmany) % 2 :
        max_val = max_val - (max_val % 100 - max_val % 10) + (max_val % 100) // 10 + (max_val % 10) * 10 -  (max_val % 10)
    print(f'#{test + 1} {max_val}')