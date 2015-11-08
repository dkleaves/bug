# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from books.models import Book

def hello(request):
    content = []
    for k, v in request.META.items():
        content.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' %  '\n'.join(content))


# def search_form(request):
#     return render_to_response('search_form.html')

def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('输入不能为空！')
        elif len(q) > 20:
            error.append('最大长度为20！')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': error})

# render为字典和列表
# def test(request):
#     dtype = {'name': 'leaves'}
#     ltype = [30,]
#     return  render_to_response('test.html', {'name': dtype, 'age': ltype})

#render为自定义类的属性
# class Person(object):
#     def __init__(self, name, age):
#         self.name, self.age = name, age
#
# def test(request):
#     return render_to_response('test.html', {'person': Person('leaves', '31')})

# for
from datetime import datetime
def test(request):
    info = ['leaves', 'mm', 'bb']
    d = datetime.now()
    return render_to_response('test.html', {'info': info, 'date': d})

def test2(request):
    return render_to_response('test2.html')