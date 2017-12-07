#encoding=utf-8
import markdown

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from taggit.models import Tag


from .models import Article, Famouswords, Comment, Category
from .forms import CommentForm
# Create your views here.

def index(request, tag_slug=None):
    article_list = Article.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    indexword = Famouswords.objects.order_by('?')[:1]
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        article_list = article_list.filter(tags__in=[tag])

    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {'articles': articles,
               'indexword': indexword,
               'categories': categories,
               'tags': tags}

    return render(request, 'index.html', context)


def article_page(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            messages.success(request, '评论已经提交')
            return HttpResponseRedirect(article.get_edit_url())
    else:
        comment_form = CommentForm()
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    context = {'article': article,
               'comments': comments,
               'comment_form': comment_form}
    return render(request, 'article_page.html', context)


def article_change(request, article_id):
    return render(request, 'article_change.html')


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})

def about_me(request):
    return render(request, 'about.html')



