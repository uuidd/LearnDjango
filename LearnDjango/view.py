from django.http import HttpResponse


def num_parameter(request, pg):
    html = '<h1>String is: {0} </h1>'.format(pg)
    return HttpResponse(html)


def cal_view(request, n, op, m):
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