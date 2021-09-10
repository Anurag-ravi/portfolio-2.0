from django.urls import path
from .views import index,send

urlpatterns = [
    path('',index, name='home'),
    path('send/',send, name='send-mail'),
]