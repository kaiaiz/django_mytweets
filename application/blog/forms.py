#encoding=utf-8
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    # widgets = {
    #     'name':forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': u'请输入昵称',
    #         'aria-describedby': 'sizing-addon1',
    #     }),
    #     'email':forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': u'请输入邮箱',
    #         'aria-describedby': 'sizing-addon1',
    #     }),
    #     'body':forms.Textarea(attrs={
    #        'placeholder': u'我来说两句',
    #     }),
    # }
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field("name", css_class='input-sm'),
            Field("email", css_class='form-control input-sm'),
            Field("body", rows="3", cols="10", css_class="input-xlarge"),
            FormActions(
                Submit('save', '提交评论', css_class='btn btn-default'),
            )
        )

