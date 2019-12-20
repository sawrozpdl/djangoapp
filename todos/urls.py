from django.urls import path
from . import views
app_name = 'todos'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('show/<slug:todoId>', views.show_todo, name = 'id'),
    path('create', views.create, name = 'create')
]