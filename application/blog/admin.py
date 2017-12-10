from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Category, Tag, Famouswords
from .models import Comment


class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content', 'author', 'created_time',
                    'status')


class CommentAdmin(SummernoteModelAdmin):
    list_display = ('article', 'name', 'email', 'created')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
