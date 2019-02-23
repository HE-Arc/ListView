from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>/', views.TeamDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
