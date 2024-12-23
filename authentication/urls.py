from django.urls import path
from .views import signUp,login,showAllUsers

urlpatterns = [path('api/signup',signUp),
path('api/show_all_users',showAllUsers),
path('api/login',login)
]