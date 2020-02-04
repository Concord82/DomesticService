from django.urls import path
import main.views as views


urlpatterns = [
    path('', views.mainpage, name='home')
]
