# -*-coding:utf-8-*-
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from online.models import TblBugList
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@csrf_exempt
def add(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('title', ''):
            errors.append("title is null")
        if not request.POST.get('level', ''):
            errors.append("level is null")
        if not request.POST.get('describe', ''):
            errors.append("describe is null")
        if not request.POST.get('experience', ''):
            errors.append("experience is null")
        if not request.POST.get('belong', ''):
            errors.append("belong is null")
        if not request.POST.get('updatetime', ''):
            errors.append("updatetime is null")
        if not errors:
            title = request.POST.get('title')
            level = request.POST.get('level')
            describe = request.POST.get('describe')
            experience = request.POST.get('experience')
            belong = request.POST.get('belong')
            updatetime = request.POST.get('updatetime')
            u = TblBugList(title=title, level=level, describe=describe, experience=experience, belong=belong, updatetime=updatetime)
            u.save()
            result = TblBugList.objects.all().order_by('-id')
            return render_to_response('list.html', {'result': result})
    return render_to_response('add.html', {'error': errors})


# @csrf_exempt
# def info(request):
#     result = TblBugList.objects.all().order_by('-id')
#     return render_to_response('list.html', {'result': result},context_instance = RequestContext(request))
def query(request):
    limit = 20
    result = TblBugList.objects.all().order_by('-id')
    paginator = Paginator(result, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        result = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        result = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        result = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('list.html', {'data': result})

def queryById(request):
    id = request.GET['id']
    if id == "": #若无输入，则转移到query查询所有
       return HttpResponseRedirect("/q")
    bb = TblBugList.objects.filter(id=id) #通过id 过滤结果，是一字典类型
    return render_to_response('list.html', {'data': bb})


@csrf_exempt
def detail(request, id):
    ONE_PAGE_OF_DATA = 20
    result = TblBugList.objects.filter(id=id)
    return render_to_response('detail.html', {'result': result})

#删除所选数据
@csrf_exempt
def delSelect(request):
     arr = request.GET['arr']
     blist="("+arr+")" # 根据列表构建元组
     TblBugList.objects.extra(where=['id IN '+str(blist)+'']).delete()
     return HttpResponse("delect success")