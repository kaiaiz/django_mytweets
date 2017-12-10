import markdown

from django import template
from django.utils.safestring import mark_safe

from blog.models import Article, Category, Tag


register = template.Library()

@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
