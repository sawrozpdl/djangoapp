from django.urls import path
from . import views
app_name = 'todos'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('show/<slug:todoId>', views.show_todo, name = 'id'),
    path('create', views.create, name = 'create'),
    path('postTodo', views.postTodo, name = 'postTodo'),
    path('<slug:todoId>/delete', views.deleteTodo, name = 'deleteTodo')
]