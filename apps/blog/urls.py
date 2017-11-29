from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index/$', views.index, name='index'),
    url(r'article/(?P<article_id>[0-9]+)$', views.article_page, name="article_page"),
    url(r'change/(?P<article_id>[0-9]+)$', views.article_change, name='edit_page'),
    url(r'tag/(?P<tag_slug>[-\w+]+)/$', views.article_page, name='post_list_by_tag'),
    url(r'change/action$', views.edit_action, name='edit_action'),
]
