from django.urls import path
from . import views




urlpatterns = [
    path('', views.index,name='index'),
    path('<int:task_id>/',views.move_goal,name='move_goal'),
     path('add_user/',views.add_user,name='add_user'),
]