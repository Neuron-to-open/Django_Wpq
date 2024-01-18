from django.shortcuts import render, redirect, HttpResponse
from app01.models import Department, UserInfo


def something(request):
    print(request.method)

    print(request.GET)
    return HttpResponse('返回内容')
# Create your views here.
def info_list(request):
    # get the all objects
    data_list = UserInfo.objects.all()
    print(data_list)
    return render(request, 'info_list.html', {'data_list': data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')

    # add into the database
    UserInfo.objects.create(name=user,
                            password=pwd,
                            age=age
                            )
    return redirect('/info/list')


def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/info/list')
