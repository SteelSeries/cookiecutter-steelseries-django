# coding: utf-8


def show_toolbar(request):
    """
    Show toolbar if cookie is set and it is not an ajax request
    """
    if request.is_ajax():
        return False

    return request.COOKIES.get('debug_toolbar') == '1'
