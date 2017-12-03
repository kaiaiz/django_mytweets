import xadmin
from xadmin import views

from taggit.models import Tag

from .models import Article, Category, Famouswords
from .models import Comment


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "Blog Management"
    site_footer = "yanchaomin'blog"
    menu_style = "accordion"


class TagInline(object):
    model = Tag
    extra = 0


class ArticleAdmin(object):
    # form = ArticleAdminForm()
    list_display = ('title', 'content', 'created_time', 'author')
    search_fields = []
    list_filter = []
    list_editable = ("author")
    prepopulated_fiels = {'slug': ('title',)}
    raw_id_fields = ('author',)
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
