from django.urls import path
from .views import say_hello, about

urlpatterns = [
    path('', say_hello, name='home'),
    path('about/', about, name='about'),
]
