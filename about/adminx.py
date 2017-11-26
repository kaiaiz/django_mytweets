from django.contrib.auth.models import User
import xadmin
from xadmin.plugins.auth import UserAdmin

from .models import UserProfile


class UserProfileAdmin(UserAdmin):
    relfield_style = 'fk-ajax'


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)

