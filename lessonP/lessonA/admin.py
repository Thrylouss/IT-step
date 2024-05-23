from django.contrib import admin
from .models import Tasks


# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')
    list_filter = ('status',)


admin.site.register(Tasks)
