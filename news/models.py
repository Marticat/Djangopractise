from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=100)
    anons = models.CharField('Anonses', max_length=250)
    full_text = models.TextField('Article text')
    date = models.DateTimeField('Date published')

    def __str__(self):
        return f'News: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Newses'