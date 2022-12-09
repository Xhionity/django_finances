from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="На что")
    content = models.FloatField(verbose_name="Сколько")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.title