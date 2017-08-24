from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_http_methods

from accounts.models import MyUser


def visual(request):
    return render(request, 'visualization/statistics.html')


@require_http_methods(["GET", "POST"])
def getSexs(request):
    if request.is_ajax():
        users = MyUser.objects.all()
        data = {
            'users': users,
        }
        return JsonResponse(data)
    else:
        raise Http404("Drama does not exist")
