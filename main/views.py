from django.shortcuts import render
from constance import config
# Create your views here.


def mainpage(request):
#    print(request.headers)
#    print(request.META)

    return render(request, 'main_page.html', {'config': config})
