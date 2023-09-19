from django.shortcuts import render
import random
# Create your views here.


def index(request):
    return render(request, 'articles/index.html')

def home(request):
    return render(request, 'home.html')

def ssafy(request):
    return render(request, 'ssafy.html')

def get_money(request):
    # 직접 변수에 값을 넣고 진행한다는듯 사용자의 입력을 받아서 채울 수 있음
    dic = {'name' : 'ssafy', \
    'account' : '012-34567-89012',\
    'money' : 40000}
    return render(request, 'articles/bank.html', context = dic)

def lotto(request):
    dic2 = {}
    for i, j in enumerate(random.sample(range(45), 6)):
        print(i, j)
        dic2['lotto' + str(i)] = str(j)
    for i, j in enumerate(random.sample(range(45), 6)):
        print(i, j)
        dic2[str(i)] = str(j)
    print(dic2)
    return render(request, 'articles/lotto.html', context = dic2)
