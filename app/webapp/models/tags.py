from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name='Тэг', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.name
