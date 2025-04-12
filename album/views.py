from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse

from album.models import Album
from user.models import MyUser


# Create your views here.
def album(request, uid):
    user = MyUser.objects.filter(id=uid).first()
    if user.id is not request.user.id:
        return redirect(reverse('toRegister'))

    album_list = Album.objects.filter(user_id=uid)

    page_size = 4
    page = request.GET.get('page', 1)  # 获取当前页码，默认是第1页
    # page分页，创建分页器
    paginator = Paginator(album_list, page_size)
    try:
        page_data = paginator.page(page)
        # print(page_data)
    except PageNotAnInteger:
        page_data = paginator.page(1)
    except EmptyPage:
        page_data = paginator.page(paginator.num_pages)

    return render(request, "album.html", locals())