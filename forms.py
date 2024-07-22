from django import forms
from django.forms import ModelForm
from .models import TodoUsers
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from captcha.fields import CaptchaField



class TodoUsersForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=10, validators=[MinLengthValidator(limit_value=6, message=">6")])
    captcha = CaptchaField()


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, label='search login')
    # text_id = forms.ModelChoiceField(queryset=TodoUsers.objects.all(), label='text_id label')
