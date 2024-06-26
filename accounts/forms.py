from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='گذرواژه', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']