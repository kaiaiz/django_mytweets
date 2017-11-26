from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, UserRegistrationForm,\
    UserProfileForm
from .models import UserProfile

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


def user_profile(request):
    initial = {'username': request.user.username,
               'nick_name': request.user.nick_name,
               'email': request.user.email,
               'mobile_number': request.user.mobile_number}
    if request.method == 'POST':
        userprofile_form = UserProfileForm(initial=initial)
        if userprofile_form.is_valid():
            nick_name = request.POST.get('mobile_number', '')
            email = request.POST.get('email', '')
            mobile_number = request.POST.get('mobile_number', '')
            user = request.user
            user.email = email
            user.save()
            return render(request,
                          "about_user.html",
                          {"userprofile_form": userprofile_form})
    else:
        userprofile_form = UserProfileForm()
    print userprofile_form
    return render(request,
                  'about_user.html',
                  {'userprofile_form': userprofile_form})

