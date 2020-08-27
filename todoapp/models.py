from django.db import models

# Create your models here.
STATUS_CHOICE = (
    ('todo', 'TO-DO'),
    ('in-progress', 'IN-PROGRESS'),
    ('done', 'DONE'),
)

class Task(models.Model):
    task_title = models.CharField(max_length=30,editable=True)
    task_details = models.CharField(max_length=100, editable=True)
    task_status = models.CharField(choices=STATUS_CHOICE, max_length=50,default='todo',editable=True)
    task_create = models.DateTimeField(auto_now_add=True)
    task_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_title