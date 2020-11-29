from django.urls import path
from user_profile import views

app_name = 'profile'
urlpatterns = [
    path('', views.ProfileView.as_view(), name='user_profile'),
    path('<int:pk>/update/', views.UpdateProfileView.as_view(), name='user_update'),
]