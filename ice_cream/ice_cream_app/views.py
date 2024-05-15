from django.shortcuts import render
from django.http import HttpResponse
from .models import Human, Child, IceCream, Shop, Order

# Create your views here.
def index(request):
    children = Child.objects.all()
    return render(request, 'ice_cream_app\index.html', {'children': children})