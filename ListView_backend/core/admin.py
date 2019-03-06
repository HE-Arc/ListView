from django.contrib import admin
from .models import Team, CustomUser, Board, List, Task

admin.site.register(Team)
admin.site.register(CustomUser)
admin.site.register(Board)
admin.site.register(List)
admin.site.register(Task)