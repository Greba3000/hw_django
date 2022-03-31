from django.contrib import admin
from news_app.models import *


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'flag']
    list_filter = ['flag']
    search_fields = ['title', 'description']  # поиск будет производиться только в указанных полях
    inlines = [CommentInLine]
    actions = ['mark_as_active', 'mark_as_not_active']

    def mark_as_active(self, request, queryset):
        queryset.update(flag='True')

    def mark_as_not_active(self, request, queryset):
        queryset.update(flag='False')

    mark_as_active.short_description = 'Опубликовать выбранные Новости'
    mark_as_not_active.short_description = 'Деактивировать выбранные Новости'


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'get_text_15_len', 'news']
    list_filter = ['author']
    actions = ['removed_by_admin']

    def removed_by_admin(self, request, queryset):
        queryset.update(text='Сообщение удалено админом! Нарушен пункт ...')

    removed_by_admin.short_description = 'Удалить выбранные Комментарии. Пункт ...'

    def get_text_15_len(self, obj):
        if len(obj.text) > 15:
            return f'{obj.text[:15]}...'
        return obj.text

    get_text_15_len.short_description = 'Комментарий'
