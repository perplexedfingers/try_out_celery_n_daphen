from django.http import HttpResponse

from .tasks import long_running_operation


def index(request):
    long_running_operation.apply_async()
    return HttpResponse("Hello, world. You're at the polls index.")
