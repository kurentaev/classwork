from django.db import models
from django.db.models import TextChoices
from django.utils import timezone

from webapp.managers import ArticleManager


class StatusChoices(TextChoices):
    ACTIVE = 'ACTIVE', 'Активна'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Не Активна'


class Article(models.Model):
    status = models.CharField(verbose_name='Статус', choices=StatusChoices.choices, max_length=100,
                              default=StatusChoices.ACTIVE)
    title = models.CharField(verbose_name='Заголовок', max_length=200, null=False, blank=False)
    text = models.TextField(verbose_name='Текст', max_length=3000, null=False, blank=False)
    author = models.CharField(verbose_name='Автор', max_length=100, null=False, blank=False, default='No name')
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    tags = models.ManyToManyField(
        to='webapp.Tag',
        related_name='articles',
        blank=True
    )

    objects = ArticleManager()

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
