from rest_framework import generics, permissions
from .models import Post, Rating
from .serializers import PostSerializer, RatingSerializer
from django.db.models import Avg
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin


class PostListView(generics.ListAPIView):
    queryset = Post.objects.annotate(average_rating=Avg('ratings__score'))
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.annotate(average_rating=Avg('ratings__score'))
    serializer_class = PostSerializer

class RatingCreateUpdateView(CreateModelMixin, generics.RetrieveUpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }