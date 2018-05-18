from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    gender = forms.CharField()
    language = forms.CharField(required=False)


    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'gender','language', 'password1', 'password2', )
