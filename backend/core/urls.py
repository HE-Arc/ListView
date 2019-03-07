from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>/', views.TeamDetail.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.UserCreate.as_view()),
    path('boards/', views.BoardList.as_view()),
    path('boards/<int:pk>/', views.BoardDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)