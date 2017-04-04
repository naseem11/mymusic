from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={
            'id': 'username',
            'class': 'form-control'

                        }))
    password = forms.CharField( widget=forms.PasswordInput(attrs={
            'id': 'password',
            'class': 'form-control'
                        }))



class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'username',
        'class': 'form-control',


    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'email',
        'class': 'form-control'
    }))

    password1 = forms.CharField( widget=forms.PasswordInput(attrs={
            'id': 'password1',
            'class': 'form-control'
                        }))

    password2 = forms.CharField(

        widget=forms.PasswordInput(attrs={
            'id': 'password-confirm',
            'class': 'form-control'
                        }))





    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance