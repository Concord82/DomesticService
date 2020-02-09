from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from person.models import Clients
# Create your views here.


def test(request):
    return render(request, '_work_base.html')

def clients(request):
    client_list = Clients.objects.only(
        'id', 'first_name', 'last_name', 'middle_name', 'phone', 'address', 'comment').order_by(
        'lastAction')[:50]

    return render(request, 'clients.html', {'clients': client_list})


def clients_search(request):
    data ={}
    if request.method == 'POST':
        clientSearch = request.POST.get('clientSearch', None)

        print(clientSearch)

        client_list = Clients.objects.filter(
            Q(phone__icontains=clientSearch) |
            Q(last_name__icontains=clientSearch)
        ).only('id', 'first_name', 'last_name', 'middle_name', 'phone', 'address', 'comment')
        json = serializers.serialize('json', client_list)

        print(json)

    return HttpResponse(json, content_type='application/json')


