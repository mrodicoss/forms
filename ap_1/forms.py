from django import forms
from .models import Book

class BookForm(forms.Form):
	title = forms.CharField(label='Ime knjige', max_length=50)
	author = forms.CharField(label='Ime autora', max_length=50)
	page_number = forms.IntegerField(label='Broj stranica')
	date = forms.DateField(label='datum izdavanja')
class BookModelForm(forms.ModelForm):#na koji model da se veze klasa iz forme.py
	class Meta:
		model = Book
		fields = ['title', 'author', 'page_number', 'date']

class BmiForm(forms.Form):
	weigth = forms.FloatField(min_value=30)
	heigth = forms.FloatField(max_value=2.5)
	gender = forms.BooleanField()

