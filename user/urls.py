from django.urls import path

from user.views import ToLogin, ToRegister, register, login, about

urlpatterns = [
    # 跳转登录页面
    path('login', ToLogin.as_view(), name="toLogin"),
    # 跳转注册页面
    path('register', ToRegister.as_view(), name="toRegister"),
    path('register/submit', register, name='register'),
    path('login/submit', login, name='login'),
    path('about', about, name="about")
]
