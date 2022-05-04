from django.urls import path
from .import views

urlpatterns = [
    path('list/',views.todo_list),
    path('insert_todo/',views.insert_todo,name='insert_todo'),
    path('delete_todoItem/<int:todo_id>',views.delete_todoItem,name = 'delete_todoItem'),
]