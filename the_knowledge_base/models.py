from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название статьи'
    )
    
    content = models.TextField(
        verbose_name='Содержание статьи'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    """def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])"""
    
    def short_content(self):
        """Краткое содержание (первые 100 символов)"""
        if len(self.content) > 100:
            return self.content[:100] + '...'
        return self.content
