#!encoding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,
                                 null=True,
                                 blank=True)
    mobile_number = models.CharField(max_length=13,
                                     null=True,
                                     blank=True,
                                     verbose_name='手机号')
    photo = models.ImageField(upload_to='about/%Y/%m/%d',
                              blank=True)
    #personal introduction
    biography = models.CharField(max_length=200,
                                 blank=True)

    class Meta:
        verbose_name = u'用户详情'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
