from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import View

from blog.models import BlogType, Blog, Comment
from user.models import MyUser


# Create your views here.
class TestView(View):
    def get(self, request):
        # 测试
        # blogtype_list_obj = BlogType.objects.all()
        # # print(type(blogtype_list_obj))
        # # <class 'django.db.models.query.QuerySet'>
        # # 转换为字典
        # blogtype_dic = blogtype_list_obj.values()
        # blogtype_list = list(blogtype_dic)
        #
        # # print(blogtype_dic)
        # # <QuerySet [{'id': 1, 'typename': 'python基础'}, {'id': 2, 'typename': '数据分析'}, {'id': 3, 'typename': '人工智能'}]>
        # # print(blogtype_list)
        # # [{'id': 1, 'typename': 'python基础'}, {'id': 2, 'typename': '数据分析'}, {'id': 3, 'typename': '人工智能'}]
        #
        # return JsonResponse({'code': 200, 'info': 'test!!!', 'data':blogtype_list})

        # 模板渲染
        return render(request, "test.html")


def blog(request, id, page, typeid):
    """
    博客信息
    :param request:
    :param id:
    :param page:
    :param typeid:
    :return:
    """
    # print(id, page, typeid)

    # 无该用户转至登陆页面
    user = MyUser.objects.filter(id=id).first()
    if user.id is not request.user.id:
        return redirect(reverse('toRegister'))

    if typeid is None or typeid == 0:
        # blog_list = Blog.objects.filter(author=request.user.id).order_by('-create_time')
        blog_list = Blog.objects.all().order_by('-create_time')
        # print(blog_list)
        # # <QuerySet [<Blog: 文字是什么1>, <Blog: 东京>, <Blog: 上海市>, <Blog: 上海市>, <Blog: 大阪>, <Blog: 东京>, <Blog: 成都市>]>
    else:
        # blog_list = Blog.objects.filter(author=request.user.id, type=typeid).order_by('-create_time')
        blog_list = Blog.objects.all().filter(type=typeid).order_by('-create_time')

    page_size = 5   # 每页大小
    # page分页
    paginator = Paginator(blog_list, page_size)
    try:
        page_data = paginator.page(page)
    except PageNotAnInteger:
        page_data = paginator.page(1)
    except EmptyPage:
        page_data = paginator.page(paginator.num_pages)
    # print(page_data)
    # # <Page 1 of 2>

    return render(request, "blogmain.html", locals())


def myblog(request, id, page, typeid):
    user = MyUser.objects.filter(id=id).first()
    if user.id is not request.user.id:
        return redirect(reverse('toRegister'))

    if typeid is None or typeid == 0:
        user_blog_list = Blog.objects.filter(author=request.user.id).order_by('-create_time')
        # print(blog_list)
        # # <QuerySet [<Blog: 文字是什么1>, <Blog: 东京>, <Blog: 上海市>, <Blog: 上海市>, <Blog: 大阪>, <Blog: 东京>, <Blog: 成都市>]>
    else:
        user_blog_list = Blog.objects.filter(author=request.user.id, type=typeid).order_by('-create_time')

    page_size = 5  # 每页大小
    # page分页
    paginator = Paginator(user_blog_list, page_size)
    try:
        page_data = paginator.page(page)
    except PageNotAnInteger:
        page_data = paginator.page(1)
    except EmptyPage:
        page_data = paginator.page(paginator.num_pages)
    # print(page_data)
    # # <Page 1 of 2>

    return render(request, "myblog.html", locals())


# 博客详情
def blog_detail(request, uid, bid):
    if request.method == "GET":
        blog = Blog.objects.filter(id=bid).first()
        user = MyUser.objects.filter(id=blog.author_id).first()

        # 阅读量 +1操作
        # F()函数在 Django中主要用于在查询表达式中引用模型的字段。它允许你在数据库层面执行各种操作，而无需将数据加载到Python内存中。
        Blog.objects.filter(id=bid).update(reads=F("reads") + 1)

        # 获取博客评论
        comment_list = Comment.objects.filter(blog_id=bid).order_by("-create_time")

        # 评论分页
        page_size = 5  # 每页大小
        page = request.GET.get('page', 1)  # 获取当前页码，默认是第1页
        # page分页，创建分页器
        paginator = Paginator(comment_list, page_size)
        try:
            page_data = paginator.page(page)
            # print(page_data)
        except PageNotAnInteger:
            page_data = paginator.page(1)
        except EmptyPage:
            page_data = paginator.page(paginator.num_pages)

        return render(request, 'blog.html', locals())
    else:
        user_info = request.POST.get("user")
        content_info = request.POST.get("content")
        kwargs = {
            "user": user_info,
            "content": content_info,
            "create_time": timezone.now(),
            "author_id": Blog.objects.filter(id=bid).first().author_id,
            "blog_id": bid
        }
        Comment.objects.create(**kwargs)
        return redirect(reverse("blog", kwargs={"uid": uid, "bid": bid}))
















