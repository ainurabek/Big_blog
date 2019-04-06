from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Companies, Post, Comments

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CompaniesForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ('name', 'address', 'contacts', 'logo', 'info')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('company','title', 'text', 'created_date', 'logo')

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('company','post', 'text', 'created_date', 'logo')

  