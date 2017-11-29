from django import forms

from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(
                                    attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(
                                    attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='first_name',
                               widget=forms.TextInput(
                                    attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email',
                               widget=forms.EmailInput(
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

