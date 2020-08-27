from django.urls import path
from todoapp import views
app_name = "todoapp"
urlpatterns = [
    path('home/', views.Homepageview.as_view(), name='home'),
    path('createtask/', views.Createtask.as_view(), name='createtask'),
    path('<int:pk>/update/', views.Updatetask.as_view(), name='update'),
    path('<int:pk>/delete/', views.Deletetask.as_view(), name='delete'),

]
