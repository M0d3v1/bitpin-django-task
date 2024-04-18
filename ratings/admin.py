from django.contrib import admin
from .models import Post, Rating

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Or any other fields you wish to display in the admin

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'score')  # Adjust fields as needed
