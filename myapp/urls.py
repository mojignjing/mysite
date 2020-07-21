"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^index/', views.index),#在views里创建index
    url(r'^hello/',views.hello),
    # url(r'$',views.index),#$路径什么都不加，访问等于index，等同于主界面
    # 走这个，后面就不走了
    # url(r'login$|regist&',views.many),#多个路径指定一个资源
    url(r'taobao/cart',views.cart),#多层级目录
    url((r'loginPage/'),views.loginPage),#今日登陆页面D
    url((r'request1/'),views.request1),
    url((r'registPage/'),views.registPage),
    url((r'doRegist/'),views.doRegist),


    # 获取模板信息
    url((r'getRegistPage/'),views.getRegistPage),
    # 转发到模板，并设置信息
    url((r'setInfo/'),views.setInfo),
    #获取后台json信息
    url((r'jsonInfo/'),views.jsonInfo),
    #转发和重定向
    url((r'login/'),views.login),
    # url(r'.',views.any),#  .  匹配任意字符串，处理错误的路径，统一返回一个样式，
    # 例如页面不存在，有先后顺序，先找上边几个

]
