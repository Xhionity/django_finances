from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="На что")
    content = models.FloatField(verbose_name="Сколько")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='admin', verbose_name="Автор", auto_created='admin')

    def __str__(self):
        return self.title