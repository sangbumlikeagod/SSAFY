from django.shortcuts import render

# Create your views here.


# 요청한 주소를 변수처럼 사용할 것이다아

def lunch(request, menu):
    lst = ['국밥']
    context = {
        'menu': menu,
               }
    
    return render(request, 'articles/lunch.html', context)

'''
기존 주소에 새롭게 요청하는 redirect도 있음
'''
def p1(request, hi, key):
    res = ''
    for i in hi:
        res += hex(int(i, 16)^int(key, 16))[2:].upper()
    # print(key
    context = {'res' : res}

    return render(request, 'articles/p1.html', context)

def throw(request):
    return render(request, 'articles/throw.html')


# 현재 form이 없는 상태 
def catch(request):
    print(request.GET)
    hi = request.GET.get('hi')
    key = request.GET.get('key')
    # context = {
    #     'hi' : hi,
    #     'key' : key
    # }
    res = ''
    for i in hi:
        res += hex(int(i, 16) ^ int(key, 16))[2:].upper()
    # print(key 
    context = {'res' : res}
    return render(request, 'articles/catch.html', context)

