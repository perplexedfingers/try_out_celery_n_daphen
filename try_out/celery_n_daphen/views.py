from django.http import HttpResponse

from .tasks import long_running_operation


def index(request):
    print('A')
    long_running_operation.apply_async()
    print('B')
    return HttpResponse("Hello, world. You're at the polls index.")
