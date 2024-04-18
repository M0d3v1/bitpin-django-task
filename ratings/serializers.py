from rest_framework import serializers
from .models import Post, Rating
from django.db.models import Avg

class PostSerializer(serializers.ModelSerializer):
    ratings_count = serializers.IntegerField(source='ratings.count', read_only=True)
    average_rating = serializers.FloatField(source='ratings__score__avg', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'ratings_count', 'average_rating']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'post', 'user', 'score']
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user  # Changed from `self.request.user`
        post = validated_data['post']
        score = validated_data['score']
        
        # 'update_or_create' handles checking if it exists and then updating or creating
        rating, created = Rating.objects.update_or_create(
            user=user, post=post, 
            defaults={'score': score}
        )
        return rating

