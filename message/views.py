from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from message.models import Message
from user.models import MyUser


# Create your views here.
def message(request, uid):
    if request.method == "GET":
        user = MyUser.objects.filter(id=uid).first()
        # if user.id is not request.user.id:
        #     return redirect(reverse('toRegister'))

        message_list = Message.objects.filter(user_id=uid).order_by('-create_time')

        page_size = 10
        page = request.GET.get('page', 1)  # 获取当前页码，默认是第1页
        # page分页，创建分页器
        paginator = Paginator(message_list, page_size)
        try:
            page_data = paginator.page(page)
            # print(page_data)
        except PageNotAnInteger:
            page_data = paginator.page(1)
        except EmptyPage:
            page_data = paginator.page(paginator.num_pages)

        return render(request, "message.html", locals())
    else:
        name_info = request.POST.get("name")
        content_info = request.POST.get("content")
        email_info = request.POST.get("email")
        kwargs = {
            "name": name_info,
            "content": content_info,
            "email": email_info,
            "create_time": timezone.now(),
            "user_id": MyUser.objects.filter(id=uid).first().id,
        }
        Message.objects.create(**kwargs)
        return redirect(reverse("message", kwargs={"uid": uid}))