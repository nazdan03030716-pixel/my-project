from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Публикация')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.text[:20]}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
