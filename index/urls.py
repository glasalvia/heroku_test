from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('telegramBot', views.activarBotTelegram, name='telegramBot'),

    
]