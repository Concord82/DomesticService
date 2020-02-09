from django.urls import path
from workpages import views

urlpatterns = [
    path('', views.clients, name='work_home'),
    path('test', views.test),

    path('ajax/clientsearch', views.clients_search),
]
