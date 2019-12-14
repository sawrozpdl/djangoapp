from django.urls import path
from . import views
app_name = 'todos'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('<slug:todoId>', views.showTodo, name = 'id'),
    path('<slug:todoId>/<str:action>', views.action, name = 'action')
]