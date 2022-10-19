from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator

from webapp.models import Article, Tag


def max_length_validator(string):
    if len(string) > 20:
        raise ValidationError("Максимальная длина строки 20 символов")
    return string


class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=20):
        message = 'Максимальное значение %(limit_value)s Вы ввели %(show_value)s символов'
        super(CustomLengthValidator, self).__init__(limit_value=limit_value, message=message)

    def compare(self, value, max_value):
        return max_value < value

    def clean(self, value):
        return len(value)



class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=123, label='Заголовок',
        validators=(
            MinLengthValidator(limit_value=2, message='aaaaaa'),
            CustomLengthValidator(limit_value=10),
        )
    )

    class Meta:
        model = Article
        fields = ('title', 'author', 'text', 'status', 'tags')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Article.objects.filter(title=title).exists():
            raise ValidationError('Запись с таким заголовком уже существует')

        return title


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')