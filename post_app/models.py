from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=500, verbose_name="Описание")
    image = models.ImageField(verbose_name="Фото")
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # post_date
