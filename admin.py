from django.contrib import admin
from .models import TodoUsers, TodoModelCreate
# Register your models here.
admin.site.register(TodoUsers)
admin.site.register(TodoModelCreate)