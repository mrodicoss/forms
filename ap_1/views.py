# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import BookForm, BookModelForm, BmiForm
from .models import Book
from .bmi import bmi_calc, BmiManager

# Create your views here.

def home(request):
	if request.method == 'GET':
		form = BookForm()
	elif request.method == 'POST':
		form = BookForm(request.POST) # bindanje forme
		if form.is_valid():
			#Book(form.cleaned_data).save()#sad ce se popuniti polja iz modela s onim sto je user submitao
			#form.cleaned_data
			#return redirect('success')
			return render(request, 'data.html', {'data': form.cleaned_data})
	context = {'form': form}
	return render(request, 'home.html', context)

def success(request):
	return render(request,'success.html')

def book(request):
	if request.method == 'GET':
		form = BookModelForm() # unbound forma
	elif request.method == 'POST':
		form = BookModelForm(request.POST) # bindanje forme
		if form.is_valid():
			form.save()

			#form.cleaned_data
			#return redirect('success')
			return render(request, 'data.html', {'data': form.cleaned_data})

	return render(request, 'book.html', {'form': form})

def update_book(request, id):
	book =Book.objects.filter(pk=id).last()
	if request.method == 'GET':		
		form = BookModelForm(instance=book)
	elif request.method == 'POST':
		form = BookModelForm(request.POST, instance=book) # boundform
		#forma je vezana uz tocno odredjeni rekord u bazi i popunit ce se podacima iz submit-ane html forme
		if form.is_valid(): # provjera je li forma validna, ako je onda se podaci mogu unjeti u bazu
			form.save()
			return render(request, 'success.html')
	context = {'form': form}
	return render(request, 'edit_book.html', context)

def bmi(request):
	if request.method == 'GET':
		form = BmiForm()
	elif request.method == 'POST':
		form = BmiForm(request.POST)
		if form.is_valid(): # ukliko je forma validna napraviti cem se izracun
			weigth = form.cleaned_data.get('weigth')
			heigth = form.cleaned_data.get('heigth')

			bmi_manager = BmiManager(weigth, heigth)
			bm_index =  bmi_manager.calculate()

			return render(request, 'success.html', {'bmi': bm_index})


	return render(request, 'bmi.html',{'form': form})


