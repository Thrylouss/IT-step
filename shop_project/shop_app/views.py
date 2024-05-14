from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def main_page(request):
    response = ""
    things = User.objects.all()
    for thing in things:
        response += str(thing.name) + "<br>"
    return HttpResponse(response)

