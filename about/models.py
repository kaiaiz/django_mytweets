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

    class Meta:
        verbose_name = u'用户详情'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
