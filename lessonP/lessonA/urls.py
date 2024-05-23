from django.urls import path

from lessonA import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('status/<int:id>', views.status, name='status'),
]