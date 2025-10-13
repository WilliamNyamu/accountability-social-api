from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.login_view, name="login"),
    path('follow/<int:user_id>/', views.follow_user, name="follow"),
    path('unfollow/<int:user_id>/', views.unfollow_user, name="follow"),
]
