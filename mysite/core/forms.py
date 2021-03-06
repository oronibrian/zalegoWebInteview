from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	LANG = (
	('Java', 'Java'),
	('C', 'C'),
	('Python', 'Python'),
	)
	Gender = (
	('male', 'Male'),
	('female', 'Female'),

	)

	gender = forms.ChoiceField(choices=Gender,widget=forms.Select(),initial='')
	language = forms.ChoiceField(choices=LANG,widget=forms.Select(),required=False,initial='')


	class Meta:
	    model = User
	    fields = ('first_name', 'last_name','username', 'gender','language', 'password1', 'password2', )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'language') #Note that we didn't mention user field here.

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile