from link.models import LinkInfo


def get_all_linkname(request):
    """
    获取当前用户所有的友情链接
    :param request:
    :return:
    """
    linkname_dict = {
        "linkname_list": LinkInfo.objects.all().filter(user=request.user.id)
    }

    return linkname_dict