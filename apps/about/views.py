from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from .forms import LoginForm, UserRegistrationForm,\
    UserProfileForm, ArticleEditForm
from .models import UserProfile
from blog.models import Famouswords, Article

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['username']
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            print user
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/blog/index')
                else:
                    return HttpResponse('Disabled account')
            else:
                 return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/blog/index')


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect('/about/login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

@login_required
def user_profile(request):
    initial = {'username': request.user.username,
               'nick_name': request.user.nick_name,
               'email': request.user.email,
               'mobile_number': request.user.mobile_number}
    if request.method == 'POST':
        userprofile_form = UserProfileForm(request.POST)
        nick_name = request.POST['name']
        mobile_number = request.POST['mobile_number']
        print mobile_number
        email = request.POST['email']
        user = request.user
        user.nick_name = nick_name
        user.mobile_number = mobile_number
        user.email = email
        user.save()
        return render(request,
                      "profile/profile.html",
                      {"userprofile_form": userprofile_form})
    else:
        userprofile_form = UserProfileForm()
    return render(request,
                  'profile/profile.html',
                  {'userprofile_form': userprofile_form})


def about_user(request):
    indexword = Famouswords.objects.order_by('?')[:1]
    context = {
        'indexword': indexword,
    }

    return render(request,
                  'profile/index.html',
                  context)

def about_settings(request):
    return render(request,
                  'profile/settings.html')

def about_messages(request):
    return render(request,
                  'profile/gallery.html')


def about_article(request):
    username = request.user.username
    user_article = Article.objects.filter(author=username)

#    if request.method == 'POST':

    context = {
        'user_article': user_article,
    }

    return render(request,
                  'profile/article.html',
                  context)


class ArticleEditView(View):
    def get(self, request, article_id):
        edit_article = get_object_or_404(Article, pk=article_id)
        init_article_form = {
            'title': edit_article.title,
            'content': edit_article.content
        }
        edit_article_form = ArticleEditForm(initial=init_article_form)

        context = {
            'edit_article': edit_article,
            'edit_article_form': edit_article_form,
        }
        return render(request,
                      'profile/article_edit.html',
                      context)
    def post(self, request, article_id):
        edit_article_form = ArticleEditForm(request.POST)

        if edit_article_form.is_valid():
            title = edit_article_form.cleaned_data['title']
            content = edit_article_form.cleaned_data['content']
            edit_article = get_object_or_404(Article, pk=article_id)
            edit_article.title = title
            edit_article.content = content
            edit_article.save()

        context = {
            'edit_article': edit_article,
            'edit_article_form': edit_article_form,
        }

        return render(request,
                      'profile/article_edit.html',
                      context)


