from django.template import loader
from django.http import HttpResponse
from .models import Todo, User


def index(request):
    searchQuery = request.POST.get('searchQuery', False)
    todos = list(filter(lambda todo : todo.containsTag(searchQuery), Todo.objects.all())) if searchQuery else Todo.objects.all()
    template = loader.get_template('todos/todos.html')
    content = {
        'title' : 'Todos by Users:',
        'todos' : todos,
        'searchQuery' : request.POST.get('searchQuery', False),
        'hasResults' : True if (len(todos) > 0) else False
    }
    return HttpResponse(template.render(content, request))

def show_todo(request, todoId):
    todo = Todo.objects.get(tid=todoId)
    template = loader.get_template('todos/todo.html')
    content = {
        'todo' : todo
    }
    return HttpResponse(template.render(content, request)) # content is the context


def create(request):
    return HttpResponse(loader.get_template('todos/createTodo.html').render({
        'guide' : 'Fill out your todo'
    }, request))


def postTodo(request):
    User.objects.all()[0].todo_set.create(title = request.POST['title'], content = request.POST['content'])    
    return HttpResponse(loader.get_template('todos/createTodo.html').render({
        'success' : 'Todo creation successful!'
    }, request))


def deleteTodo(request, todoId):
    Todo.objects.get(tid=todoId).delete()
    todos = Todo.objects.all()
    template = loader.get_template('todos/todos.html')
    content = {
        'title' : 'Todos by Users:',
        'todos' : todos,
        'success' : 'todo deletion successfull!'
    }
    return HttpResponse(template.render(content, request))
    