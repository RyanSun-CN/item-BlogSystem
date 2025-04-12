from django.urls import path
from django.views.generic import RedirectView

from blog.views import TestView, blog, blog_detail, myblog

urlpatterns = [
    # path('test', TestView.as_view(), name='test'),
    path('', RedirectView.as_view(url='user/login')),
    path('blogmain/<int:id>/<int:page>/<int:typeid>', blog, name='blogmain'),
    path('blog/<int:uid>/<int:bid>', blog_detail, name='blog'),
    path('myblog/<int:id>/<int:page>/<int:typeid>', myblog, name="myblog")
]
