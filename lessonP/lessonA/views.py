from django.shortcuts import render
from .models import Tasks


# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'lessonA/index.html', context=context)


def delete(request, id):
    task = Tasks.objects.get(id=id)
    task.delete()
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'lessonA/index.html', context=context)


def status(request, id):
    task = Tasks.objects.get(id=id)
    task.status = True
    task.save()
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'lessonA/index.html', context=context)