#encoding=utf-8
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

#    widgets = {
#        'name':forms.TextInput(attrs={
#            'class': 'form-control',
#            'placeholder': u'请输入昵称',
#            'aria-describedby': 'sizing-addon1',
#        }),
#        'email':forms.TextInput(attrs={
#            'class': 'form-control',
#            'placeholder': u'请输入邮箱',
#            'aria-describedby': 'sizing-addon1',
#        }),
#        'body':forms.Textarea(attrs={
#            'placeholder': u'我来说两句',
#        }),
#    }

