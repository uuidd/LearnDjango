from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def num_parameter(request, pg):
    html = '<h1>String is: {0} </h1>'.format(pg)
    return HttpResponse(html)


def cal_view(request, n, op, m):
    result = 0
    if op not in ['add', 'mul', 'sub']:
        html = '<h1>输入错误！</h1>'
    else:
        if op == 'add':
            result = n + m
        elif op == 'sub':
            result = n - m
        elif op == 'mul':
            result = n * m
        html = '<h1>计算结果为： {0}</h1>'.format(result)
    return HttpResponse(html)


def cal_re_view(request, op, x, y):
    if op == 'add':
        result = int(x) + int(y)
        html = '<h1>计算结果为： {0}</h1>'.format(result)
    else:
        html = '<h1>输入错误！</h1>'
    return HttpResponse(html)


def request_view(request, g):
    param1 = request.GET
    print(param1)
    html = f'<h1>test param: {param1.a}</h1>'
    return HttpResponse(html)


def get_view(request):
    print(request.GET)
    print(request.GET['a'])
    print(request.GET.get('a', 'no a'))
    print(request.GET.getlist('a'))
    # http: // 127.0.0.1:8000/get/?a = 1 & a = 2
    # < QueryDict: {'a': ['1', '2']} >
    # 2
    # 2
    # ['1', '2']
    return HttpResponse('GET')


def post_view(request):
    post_form = """
        <form method='post' action='/test-post'>
            user_name:<input type='text' name='user_name'>
            <input type='submit' value='submit'>
        </form>
    """
    return HttpResponse(post_form)


def test_post_view(request):
    user_name = ''
    if request.method == 'POST':
        user_name = request.POST['user_name']
    html = f'<h1>USER NAME: {user_name}</h1>'
    return HttpResponse(html)


def templates_view(request):
    t = loader.get_template("test_templates.html")
    html = t.render()
    return HttpResponse(html)


def templates_view2(request):
    dic = {
        'user_name': 'name'
    }
    return render(request, 'test_templates.html', dic)


def param_view(request):
    def say_hi():
        return 'hello'

    class Dog:
        def say(self):
            return '汪汪'

    dic = {}
    dic['int'] = 88
    dic['str'] = 'test'
    dic['lst'] = ['tom', 'jack', 'lily']
    dic['dict'] = {'a': 9, 'b': 8}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    return render(request, 'test_param.html', dic)


def test_my_cal(request):
    if request.method == 'GET':
        return render(request, 'myCal.html')
    elif request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y

        return render(request, 'myCal.html', locals())
