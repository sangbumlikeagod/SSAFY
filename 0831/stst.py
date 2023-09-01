import sys


name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file
test_case = int(input())



def fienfien(i, dic, sum):
    if not dic:
        return False
    
    for k in dic:
        return
    
    new = dic.copy()
    return

    
    fienfien(new)
    

    



for num in range(test_case):
    return_value = 0
    N, K = map(int, input().split())
    dic = {}
    for i in list(map(int, input().split())):
        dic[i] = dic.get(i, 0) + 1 

    for i in dic:
        new = dic.copy()
        fienfien(i, new)


    print(f'#{num + 1} {return_value}')