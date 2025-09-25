from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add/',views.add,name='add'),
    path('add_todo/',views.add_todo,name='add_todo'),
    path('delete_todo/<int:id>/',views.delete_todo,name='delete'),
    # path('update_path/<int:id>/',views.update,name='update'),
    path('update_todo/<int:id>/',views.update_todo,name='update_todo')

]
