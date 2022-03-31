from django.db import models


class News(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',
                                      editable=True)  # без editable=True не отобразит в админке
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования', editable=True)
    flag = models.BooleanField(default=True, verbose_name='Статус публикации')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at'] # в обратном порядке "-"
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    author = models.CharField(max_length=50, verbose_name='Автор')
    text = models.CharField(max_length=200, verbose_name='Текст комментария')
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE,
                             related_name='comment',
                             verbose_name='Новость')  # related new change comment_set for comment

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
