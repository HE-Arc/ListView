from django.urls import path,include

from auth0 import views

urlpatterns = [
    path('users/', views.UserGetId.as_view()),
    path('users/<int:pk>/', views.UserUpdate.as_view()),
]