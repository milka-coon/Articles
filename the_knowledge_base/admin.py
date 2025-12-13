from django.contrib import admin
from django.utils.html import format_html
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'short_content_display', 
        'created_at_formatted', 
        'updated_at_formatted', 
        'is_published',
        'name_display'
    )
    
    list_filter = (
        'is_published',
        'created_at',
        'updated_at',
        'category__name'
    )
    
    search_fields = (
        'title',
        'content',
        'category__name'
    )
    
    list_editable = ('is_published',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content', 'is_published', 'category')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    # Форматирование дат в списке
    def created_at_formatted(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    created_at_formatted.short_description = 'Дата создания'
    
    def updated_at_formatted(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    updated_at_formatted.short_description = 'Дата обновления'
    
    # Краткое содержание в списке
    def short_content_display(self, obj):
        return obj.short_content()
    short_content_display.short_description = 'Краткое содержание'
    
    # Поиск по дате
    date_hierarchy = 'created_at'
    
    #Отображение categories
    def name_display(self, obj):
        if obj.category: 
            return obj.category.name 
        else:
            return 'не указан'
    name_display.short_description = 'Категория'
    



admin.site.register(Article, ArticleAdmin)