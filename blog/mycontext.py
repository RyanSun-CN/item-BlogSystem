"""
上下文
"""
from blog.models import BlogType


def get_all_blogtype(request):
    """
    获取 blog类别
    :return: dict
    """
    blogtype_dict = {
        # 获取当前用户的 ID
        # "user_id": request.user.id,
        # 仅获取当前用户的日志类别
        "blogtype_list": BlogType.objects.all(),
    }

    # print(request.user.id, BlogType.objects.all().filter(user=request.user.id))

    # print(BlogType.objects.all())
    # # <QuerySet [<BlogType: python基础>, <BlogType: 数据分析>, <BlogType: 人工智能>]>
    #  BlogType.objects.all() 返回 BlogType 模型的对象实例，所以默认会调用模型的 __str__() 方法来展示对象

    # print(BlogType.objects.values())
    # # <QuerySet [{'id': 1, 'typename': 'python基础', 'user_id': 1}, {'id': 2, 'typename': '数据分析', 'user_id': 2}, {'id': 3, 'typename': '人工智能', 'user_id': 1}]>
    # BlogType.objects.values()直接返回 字典格式的数据

    # print(blogtype_dict.values())
    # # dict_values([<QuerySet [<BlogType: python基础>, <BlogType: 数据分析>, <BlogType: 人工智能>]>])
    return blogtype_dict

