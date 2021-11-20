
# Register your models here.
from django.contrib import admin
from .models import Task

class TaskList(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'rating')
    list_filter = ('name', 'year', 'rating')
    search_fields = ('name', 'description')
    ordering = ['year']


admin.site.register(Task, TaskList)
