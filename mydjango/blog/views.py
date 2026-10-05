from django.http import HttpResponse


def post_list(request):
    return HttpResponse('Список постов блога. Приложение blog')


def post_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}. Приложение blog')
