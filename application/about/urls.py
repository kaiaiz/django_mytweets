from django.conf.urls import url, include

from . import views
from .views import (ArticleEditView, ArticleView,
                    ArticleCreateView)


urlpatterns = [
    url(r'login/$', views.user_login, name='login'),
    url(r'logout/$', views.user_logout, name='logout'),
    url(r'register/$', views.user_register, name='register'),
    url(r'profile/$', views.user_profile, name='profile'),
    url(r'about_user/$', views.about_user, name='about_user'),
    url(r'settings/$', views.about_settings, name='about_settings'),
    url(r'messages/$', views.about_messages, name='messages'),
    url(r'article/$', ArticleView.as_view(), name='article'),
    url(r'article-create/$', ArticleCreateView.as_view(), name='article_create'),
    url(r'article-edit/(?P<article_id>[0-9]+)$', ArticleEditView.as_view(),
        name='article_edit'),
]

