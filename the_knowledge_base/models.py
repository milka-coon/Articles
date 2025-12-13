from django.db import models
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    """Модель категории/группы для статей"""
    name = models.CharField(
        max_length=200, 
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=200, 
        unique=True, 
        verbose_name='URL-идентификатор',
        help_text='Уникальная часть URL (например, "programming-tips")'
    )
    description = models.TextField(
        blank=True, 
        verbose_name='Описание категории',
        help_text='Необязательное описание категории'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания'
    )
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']  # Сортировка по алфавиту
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    def article_count(self):
        """Количество статей в категории"""
        return self.articles.count()


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название статьи'
    )
    
    content = models.TextField(
        verbose_name='Содержание статьи'
    )
    
    
    category = models.ForeignKey(
        Category,  # Ссылка на модель Category, которую мы определили выше
        on_delete=models.SET_NULL,  # При удалении категории у статей будет category=NULL
        null=True,  # Разрешаем NULL в базе данных
        blank=True,  # Разрешаем пустое значение в формах админки
        related_name='articles',  # Обратная связь: category.articles.all()
        verbose_name='Категория',
        help_text='Выберите категорию для статьи'
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
        ordering = ['-created_at']  # Новые статьи первыми
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
    
    # Дополнительные полезные методы
    def get_category_name(self):
        """Получить название категории или 'Без категории'"""
        return self.category.name if self.category else 'Без категории'
    
    def is_recently_updated(self):
        """Проверка, обновлялась ли статья за последние 7 дней"""
        return (timezone.now() - self.updated_at).days < 7
    
    
    def short_content(self):
        """Краткое описание статьи"""
        return self.content[:101]