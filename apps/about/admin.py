from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    list_display = ('username', 'email', 'is_active', 'is_staff',
                    'last_login')

admin.site.register(UserProfile, UserProfileAdmin)
