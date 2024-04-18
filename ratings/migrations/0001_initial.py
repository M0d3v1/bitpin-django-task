# Generated by Django 5.0.4 on 2024-04-18 06:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the post.', max_length=100)),
                ('description', models.TextField(help_text='Detailed description of the post.')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='The score given by the user, from 0 to 5.')),
                ('post', models.ForeignKey(help_text='The post that this rating relates to.', on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='ratings.post')),
                ('user', models.ForeignKey(help_text='The user who gave the rating.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
