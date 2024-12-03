from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addTodoItem, name='addTodoItem'),
    path('complete/<int:todo_id>/', views.completedTodo, name='completedTodo'),
    path('delete-completed/', views.deletecompleted, name='deletecompleted'),
    path('delete-all/', views.deleteAll, name='deleteAll'),
]