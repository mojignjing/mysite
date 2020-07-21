from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader, RequestContext


def index(request):
    return HttpResponse("Hello word")
def hello(request):
    return HttpResponse('哈哈哈')
# def any(request):
#     return HttpResponse('不管访问什么，都是我')
def many(request):
    return HttpResponse("多个路径指定一个资源")
def cart(request):
    return HttpResponse('cart')
#借助模板
def loginPage(request):
    return render(request,template_name="myapp/loginPage.html")

#request对象基本信息
def request1(request):
    # request=HttpRequest()
    print(request.path)
    print(request.method)
    print(request.body)
    return HttpResponse('12345678')

#request获取get请求对象
def registPage(request):
    return render(request,template_name="myapp/registPage.html")

def doRegist(request):
    # request=HttpRequest()
    # print(request.GET.get("username"))
    # print(request.GET.get("password"))
    # print(request.GET.getlist("hobby"))
    # request=HttpRequest()
    # print(request.POST.get("username"))
    # print(request.POST.get("password"))
    # print(request.POST.getlist("hobby"))
    requestMethod=None
    if request.method=="GET":
        requestMethod=request.GET
    elif request.method=="POST":
        requestMethod=request.POST
    username=requestMethod.get("username")
    password=requestMethod.get("password")
    hobby=requestMethod.getlist("hobby")
    print(username,password,hobby)

    return HttpResponse('注册成功')

# 加载模板写法，等同于render(request,template_name="myapp/registPage.html")
#只做了解
def getRegistPage(request):
    t1=loader.get_template("myapp/registPage.html")
    context=RequestContext(request)
    return HttpResponse(t1.render(context))


def setInfo(request):
    name=request.GET.get("name1")
    return render(request,"myapp/info.html",context={"name1":name})


def jsonInfo(request):
    lists=[
        {"username": "张三", "sex": "男", "age": 18}, {"username": "李四", "sex": "男", "age": 18},
        {"username": "王五", "sex": "男", "age": 18}]


    return JsonResponse({"lists1":lists})


def login(request):
    #转发，从一个路径转换到另一个路径，属于1次请求，
    # 如果刷新页面，先执行开始的逻辑，在执行后边转发的逻辑

    # return hello(request)
    # 重定向,从一个路径可以重定向到另一个路径，属于两次请求
    #如果刷新页面，只执行当前逻辑
    #登录-主页，使用重定向
    # 查询商品信息，展示到页面上，转发

    return redirect("/hello/")