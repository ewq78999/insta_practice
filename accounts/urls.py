from django.urls import path
from . import views

app_name = 'accounts'

ulrpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('<str:username>', views.profile, name='profile'),
]