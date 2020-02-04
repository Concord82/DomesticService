from django.shortcuts import render
from constance import config
# Create your views here.


def mainpage(request):
    print(request.headers)
    print(request.META)

    print (config.Phone_Number)
    return render(request, '_base_main.html', {'config': config})
