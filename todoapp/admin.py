from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display =('task_title', 'task_details','task_status','task_create','task_update')

