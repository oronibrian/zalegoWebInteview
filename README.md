# Zalego web Interview

## Developed using django 

#### Sample code
```python
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



```

## Instruction to run
1.Clone repo
2.Install requiremets.txt
3.python manage.py runserver