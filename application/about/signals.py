from django.db.models.signals import post_save

from notifications.signals import notify

from blog.models import Comment


def my_handler(sender, instance, created, **kwargs):
    notify.send(instance, verb='was commented')


post_save.connect(my_handler, sender=Comment)
