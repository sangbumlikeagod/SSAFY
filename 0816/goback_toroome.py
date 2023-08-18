import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())

'''
주어진 요구사항 원래 N이 걸릴 이동 시간에서 
한 학생이 가려는 방 - 1 이후의 방에서 출발하려는 할생들이 있다면 그 학생들은 
동시에 움직일 수 있다.

어떤 학생의 끝과 다른 학생의 시작이 겹치지 않는지 안겹친다면 최대 얼마나 안겹치는
학생들이 있을 수 있는지를 확인하라 

어떤 학생을 기준으로 안겹치는지 확인하는 것은 불가능하다. 안겹친다고 확인했던 
요소 두개가 겹칠 수 있기 때문 즉 서로 겹치지 않는 요소들만 넣을 수 있다.

또 정렬돼있다는 얘기가 없으니까 정렬을 해주던 해야됨

맨 마지막꺼를 가져가서 시작점이 마지막 애 끝점과 겹치면 다른데 추가하고
안겹칠 때만 그 리스트에 추가함

이 방식은 통하지 않는다.

그럼 겹치는 애들을 모두 구하고 겹치는 애가 많은 애부터 삭제해서 비게 하자 
'''
#
# for num in range(test_case):
#     students = int(input())
#     # students = 4
#     return_value = 0
#     lst = []
#     for _ in range(students):
#         new = list(map(int, input().split()))
#         if new[0] > new[1]:
#             new[0], new[1] = new[1], new[0]
#         lst.append(new)
#     lst.sort(key = lambda x : x[0])
#
#     # 뒤에서 부터 정렬한 다음에 다 뺌
#     print(lst)
#     while lst:
#         stack1 = []
#         stack2 = []
#         stack2.append(lst.pop())
#         while lst:
#             # print(stack2)
#             a = lst.pop()
#             if a[1] <= stack2[-1][1] and stack2[-1][0] <= a[0]:
#                 stack1.append(stack2.pop())
#                 stack2.append(a)
#             elif a[1] < stack2[-1][0]:
#                 stack2.append(a)
#             else:
#                 stack1.append(a)
#         else:
#             # print(stack1)
#             lst = stack1
#             return_value += 1
#
#
#
#
#     print(f'#{num + 1} {return_value}')




for num in range(test_case):
    students = int(input())
    return_value = 0
    dic = {}
    for _ in range(students):
        a, b = map(int, input().split())
        if b < a:
            a, b = b, a
        if b % 2:
            b += 1
        if not a % 2:
            a -= 1
        new = (a, b)
        so_far = list(dic.keys())
        for arg in so_far:
            if arg[0] <= new[0] and not arg[1] <= new[0]:
                dic[arg].append(new)
                dic[new] = dic.get(new, []) + [arg]
            elif new[0] <= arg[0] and not new[1] <= arg[0]:
                dic[arg] = dic.get(arg, []) + [new]
                dic[new] = dic.get(new, []) + [arg]
        dic[new] = dic.get(new, [])
    # 제일 많이 겹친애부터 가는데 걔랑 안겹치는 애가 있으면 같이가도 무방하지
    print(dic)
    while sum([len(dic[i]) for i in dic]):
        maxx = []
        for case in dic:
            if len(dic[case]) > len(maxx):
                idx = case
                maxx = dic[case]
        for i in dic[idx]:
            dic[i].remove(idx)
        dic.pop(idx)
        return_value += 1
    print(dic)

    if dic:
        return_value += 1

    print(f'#{num + 1} {return_value}')