from django.template import loader
from django.http import HttpResponse
from .models import Todo, User


def index(request):
    todos = Todo.objects.all()
    template = loader.get_template('todos/index.html')
    content = {
        'title' : 'Todos Created by users across this site',
        'todos' : todos
    }
    return HttpResponse(template.render(content, request))

def showTodo(request, todoId):
    todo = Todo.objects.get(tid=todoId);
    template = loader.get_template('todos/todo.html')
    content = {
        'todo' : todo
    }
    return HttpResponse(template.render(content, request)) # content is the context

def action(request, todoId, action):
    return HttpResponse('You are Doing action: {action} viewing : {id}'.format(id=todoId, action=action))