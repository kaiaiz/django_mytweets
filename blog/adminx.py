import xadmin
from xadmin import views

from .models import Article, Category, Tag, Famouswords
from .models import Comment


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "Django Management"
    site_footer = "yanchaomin'blog"
    menu_style = "accordion"


class AuthorInline(object):
    model = Article
    extra = 0


class ArticleAdmin(object):
    # form = ArticleAdminForm()
    list_display = ('title', 'content', 'created_time', 'author')
    search_fields = []
    list_filter = []
    list_editable = ("author")
    #inlines = [AuthorInline]


class CommentAdmin(object):
    list_display = ('article', 'name')

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Category)
xadmin.site.register(Tag)
xadmin.site.register(Famouswords)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSetting)
