from django.shortcuts import render

def say_hello(request):
    return render(request, 'lesson_app/index.html')

def about(request):
    return render(request, 'lesson_app/about.html')
