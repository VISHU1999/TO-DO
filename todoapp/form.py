# from django import forms
# from todoapp.models import *
#
# STATUS_CHOICE = (
#     ('todo', 'TO-DO'),
#     ('in-progress', 'IN-PROGRESS'),
#     ('done', 'DONE'),
# )
#
# class Creattask(forms.Form):
#     task_title = forms.CharField(max_length=30, required=True, )
#     task_details = forms.CharField(max_length=100, )
#     task_status = forms.ChoiceField(status=STATUS_CHOICE, default='todo')
#     task_create = forms.DateTimeField(auto_now_add=True)
#     #task_update = forms.DateTimeField(auto_now=True)
#
#
