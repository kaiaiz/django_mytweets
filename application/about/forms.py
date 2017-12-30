# encoding=utf-8

from __future__ import absolute_import
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions

from .models import UserProfile
from blog.models import Article


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field("username", css_class='form-control'),
            Field("password", css_class='form-control'),
            FormActions(
                Submit('submit', '登录', css_class='btn btn-default'),
            )
        )


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='first_name',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'nick_name', 'email',
                  'mobile_number')


class ArticleEditForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super(ArticleEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field("title"),
            Field("content"),
            Field("tags", '标签'),
            FormActions(
                Submit('save', '保存'),
            )
        )


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'slug', 'category', 'status', 'tags']

    def __init__(self, *args, **kwargs):
        super(ArticleCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field("title", '标题'),
            Field("content", '内容'),
            Field("slug", ),
            Field("status", '状态'),
            Field("category", '目录'),
            Field("tags", '标签'),
            FormActions(
                Submit('save', '创建'),
            )
        )



