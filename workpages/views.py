from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from person.models import Clients
# Create your views here.


def clients(request):
    return render(request, 'clients.html')


def clients_search(request):
    data ={}
    if request.method == 'POST':
        clientSearch = request.POST.get('clientSearch', None)

        print(clientSearch)

        client_list = Clients.objects.filter(
            phone__icontains=clientSearch
        )
        json = serializers.serialize('json', client_list)

    return HttpResponse(json, content_type='application/json')


