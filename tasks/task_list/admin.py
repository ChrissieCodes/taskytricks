from django.contrib import admin
from .models import Task
from .models import Tag
# Register your models here.
admin.site.register(Task)
admin.site.register(Tag)