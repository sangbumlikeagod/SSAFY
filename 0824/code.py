import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())
# test_case = 1

# def
def check(string):
    return (bin(int(string, 16))[2:])

for num in range(test_case):
    # if num == 12:
    #     continue
    return_value = 0
    N, M = map(int, input().split())
    lst = set(input().strip().strip('0') for _ in range(N))
    # print(lst)
    dic = {
        13: 0,
        25: 1,
        19: 2,
        61: 3,
        35: 4,
        49: 5,
        47: 6,
        59: 7,
        55: 8,
        11: 9
    }
    new_lst = []
    while True:
        for i in lst:
            contin_0 = 0
            size = len(i)
            idx = 0
            tmp = 0
            for j in range(len(i)):
                if i[j] == '0':
                    tmp += 1
                else:
                    if tmp > contin_0:
                        contin_0 = tmp
                    tmp = 0
            if contin_0 >= 4:

                for new in i.split('0' * (contin_0)):
                    new.strip('0')
                    new_lst.append(new)
            else:
                new_lst.append(i)
        if len(lst) == len(new_lst):
            break
        else:
            lst, new_lst = new_lst[:], []

    print(lst)

    suspect = []
    # 최대로 반복될 수 있는 0의 길이는 애의 길이 // 56한것과 얼추 비슷할 것
    for i in new_lst:
        if i and i not in suspect:
            suspect.append(i)
    print(suspect)
    for j in suspect:
        tmp = check(j).rstrip('0')
        while len(tmp) % 56:
            tmp = '0' + tmp
        step = len(tmp) // 56
        # print(tmp)
        k = -1
        ans = []
        while k > -56 * step - 1:
            ss = 0
            local = 0
            for case in range(7):
                local += int(tmp[k]) << ss
                ss += 1
                k -= step
            ans.append(dic[local])
        print(ans)
        if not (ans[0] + (ans[1] + ans[3] + ans[5] + ans[7]) * 3 + (ans[2] + ans[4] + ans[6])) % 10:
            return_value += ans[0] + ans[1] + ans[3] + ans[5] + ans[7] + ans[2] + ans[4] +ans[6]
            continue
    print(f'#{num + 1} {return_value}')


