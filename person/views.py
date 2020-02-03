from django.shortcuts import render

# Create your views here.


def home(request):
    print(request.headers)
    print(request.META)
    return render(request, 'test.html')