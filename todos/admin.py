from django.contrib import admin
from todos.models import User, Todo
# Register your models here.

admin.site.register(User)
admin.site.register(Todo)