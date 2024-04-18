from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the post.")
    description = models.TextField(help_text="Detailed description of the post.")
    
class Rating(models.Model):
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE, help_text="The post that this rating relates to.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user who gave the rating.")
    score = models.IntegerField(choices=[(i, i) for i in range(6)], help_text="The score given by the user, from 0 to 5.")
    
    class Meta:
        unique_together = (('user', 'post'),)
        