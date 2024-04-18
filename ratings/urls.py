from django.urls import path, include 
from .views import PostListView, PostDetailView, RatingCreateUpdateView

urlpatterns = [
    path('ratings/<int:pk>/', RatingCreateUpdateView.as_view(), name='rating-create-update'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
    
]
