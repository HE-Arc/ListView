from django.contrib import admin
from .models import Team, CustomUser, Board

admin.site.register(Team)
admin.site.register(CustomUser)
admin.site.register(Board)