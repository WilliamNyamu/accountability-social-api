from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name="list-posts"),
    path('posts/create/', views.PostCreateView.as_view(), name="create-post"),
    path('posts/<int:pk>/retrieve/', views.PostRetrieveView.as_view(), name="retrieve-post"),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name="update-post"),
    path('posts/<int:pk>/delete/', views.PostDestroyView.as_view(), name="delete-post"),
]