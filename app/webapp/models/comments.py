from django.db import models


class Comment(models.Model):
    article = models.ForeignKey(
        to='webapp.Article',
        verbose_name='Статья',
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.CharField(
        verbose_name='Автор',
        null=True,
        default='Anonimous',
        max_length=40
    )
    text = models.TextField(
        verbose_name='Комментарий',
        max_length=400
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Запись создана'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Запись изменена'
    )

    def __str__(self):
        return f'{self.author} : {self.text[:30]}'
