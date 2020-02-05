from django.urls import path
from workpages import views

urlpatterns = [
    path('', views.clients, name='work_home')
]
