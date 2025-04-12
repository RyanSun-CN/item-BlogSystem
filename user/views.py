from django.contrib import auth
from django.contrib.auth import logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from user.models import MyUser


# Create your views here.

# 基于类的视图 CBV
# 继承自 View，用于处理 HTTP 请求（GET、POST 等）。
# get(self, request) 仅处理 GET 请求。需要在 urls.py 中使用 .as_view() 绑定
# 适用于复杂的逻辑
class ToLogin(View):
    def get(self, request):
        return render(request, "login.html")


class ToRegister(View):
    def get(self, request):
        return render(request, "register.html")


# 基于函数的视图 FBV
# 直接定义一个普通 Python 函数，接受 request 作为参数。
# 适用于简单的视图，不需要额外的类结构。处理 GET和 POST需要手动判断。
# 在 urls.py 中直接使用，不用.as_view()绑定

def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    info = None
    username = ''

    if request.method == "POST":
        # 表单 name属性对应，method="post"
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        # 结合前端验证
        if MyUser.objects.filter(username=username):
            info = "用户名已存在！\n请更改用户名！"
            username = ''
        elif password2 != password:
            info = "密码不一致！\n请确认二次密码输入正确！"
        else:
            user_dict = {
                'username': username,
                'password': password,
                'is_superuser': 1,
                'is_staff': 1
            }
            # **user_dict解包字典，将键值对作为关键字参数传入。
            # 返回模型对象
            user = MyUser.objects.create_user(**user_dict)
            user.save()
            # print(type(user))
            # # <class 'user.models.MyUser'>

            info = "注册成功！\n请重新登录！"
            # 清除当前会话中的所有用户信息，使用户退出登录
            logout(request)
            return redirect('toLogin')

    # info = 'GET'
    return render(request,
                  "register.html",
                  {"info": info, "username": username})


def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        errorinfo = ""
        if MyUser.objects.filter(username=username):
            # print(MyUser.objects.filter(username=username))
            # # <QuerySet [<MyUser: 匿名用户>]>
            # 检查给定的用户名和密码是否与数据库或某个认证系统中的记录匹配。
            # 如果匹配，意味着用户身份合法，可以继续执行后续操作；如果不匹配，则通常会返回错误或者提示用户身份验证失败
            user = authenticate(username=username, password=password)
            # print(user)
            # # 匿名用户
            if user:
                if user.is_active:
                    # print(user.is_active)
                    # # True

                    auth.login(request, user)
                    # print(auth.login(request, user))
                    # # None

                    # print("登陆验证成功")
                    kwargs = {
                        "id": request.user.id,
                        "page": 1,
                        "typeid": 0
                    }
                    return redirect(reverse("blogmain", kwargs=kwargs))
                else:
                    errorinfo = "用户被禁止登陆"
            else:
                errorinfo = "用户名/密码不正确"
        else:
            errorinfo = "用户名不存在！\n请注册！"

        return render(request, "login.html", {"errorinfo": errorinfo})

    return redirect(reverse("toLogin"))


def about(request):
    user = MyUser.objects.filter(id=request.user.id).first()
    return render(request, "about.html", locals())

