from django.views.defaults import page_not_found


def page_not_found_view(request, exception):
    return page_not_found(request, '404.html', status=404)
