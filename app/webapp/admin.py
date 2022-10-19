from django.contrib import admin

from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_filter = ('id', 'title', 'author', 'created_at')
    search_fields = ('title', 'author')
    fields = ('title', 'author', 'text', 'created_at', 'changed_at')
    readonly_fields = ('id',)


admin.site.register(Article, ArticleAdmin)
