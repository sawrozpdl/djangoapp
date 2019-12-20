from django.template import loader
from django.http import HttpResponse
from .models import Todo, User


def index(request):
    todos = Todo.objects.all()
    template = loader.get_template('todos/todos.html')
    content = {
        'title' : 'Todos by Users:',
        'todos' : todos
    }
    return HttpResponse(template.render(content, request))

def show_todo(request, todoId):
    todo = Todo.objects.get(tid=todoId);
    template = loader.get_template('todos/todo.html')
    content = {
        'todo' : todo
    }
    return HttpResponse(template.render(content, request)) # content is the context


def create(request):
    return HttpResponse(loader.get_template('todos/createTodo.html').render({
        'guide' : 'Fill out your todo'
    }, request))