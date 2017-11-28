#encoding=utf-8
from __future__ import unicode_literals

import markdown
from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


from simditor.fields import RichTextField
from taggit.managers import TaggableManager

from about.models import UserProfile


# Create your models here.
class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager,
                     self).get_queryset().filter(status='created_time')


class Category(models.Model):
    name = models.CharField(max_length=100,
                            null=True,
                            default="")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'目录'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=100,
                            null=True,
                            default="")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    articleauthor = UserProfile.objects.all()

    ARTICLE_AUTHOR_CHOICES = [(str(user), str(user)) for user in articleauthor]


    title = models.CharField(max_length=70,
                             default="title")
    content = RichTextField()
    tags = TaggableManager()
    slug = models.SlugField(default=tags)
    created_time = models.DateField(default=datetime.now)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category,
                                 blank=True,
                                 null=True)
    author = models.CharField(choices=ARTICLE_AUTHOR_CHOICES,
                              max_length=30,
                              default='')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
#    published = ArticleManager()

    def save(self, *args, **kwargs):
        self.excerpt = self.content[:54]
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_page', kwargs={'article_id': self.id})

    class Meta:
        ordering = ('created_time',)
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Famouswords(models.Model):
    body = models.TextField(max_length=120, blank=True)
    author = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.body[:10]

    class Meta:
        verbose_name = u'名言警句'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments')
    name = models.CharField(max_length=80,
                            verbose_name=u'姓名')
    email = models.EmailField(verbose_name=u'邮件')
    body = models.TextField(verbose_name=u'内容')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = u'评论'
        verbose_name_plural = verbose_name


    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.article)


print settings.AUTH_USER_MODEL
