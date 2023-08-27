from django import forms
from .models import Comment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nickname', 'email', 'content')

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email", )