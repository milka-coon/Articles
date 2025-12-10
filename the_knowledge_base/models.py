from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


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
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    
    def short_content(self):
        """Краткое содержание (первые 100 символов)"""
        if len(self.content) > 100:
            return self.content[:100] + '...'
        return self.content

"""class Category(models.Model):
    #Категория/группа для статей
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории',
        unique=True
    )
    
    slug = models.SlugField(
        max_length=100,
        verbose_name='URL-адрес категории',
        unique=True,
        blank=True
    )
    
    description = models.TextField(
        verbose_name='Описание категории',
        blank=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('articles_by_category', args=[self.slug])
    
    def get_article_count(self):
        return self.articles.count()

class Article(models.Model):
    # ... существующие поля ...
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
        verbose_name='Категория'
    )
    
    # ... остальные методы ...
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id), self.slug])"""