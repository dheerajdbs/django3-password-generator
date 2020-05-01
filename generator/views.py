from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
	return render(request,'generator/home.html')

def password(request):

	characters = 'abcdefghijklmnopqrstuvwxyz'

	if request.GET.get('uppercase'):
		characters += characters.upper()

	if request.GET.get('special'):
		characters += '!@#$%^&*'

	if request.GET.get('numbers'):
		characters += '0123456789'

	length = int(request.GET.get("length" , 12))

	thepassword = ''

	for x in range(length):
		thepassword +=  random.choice(characters)

	return render(request,'generator/password.html',{'password': thepassword})

def about(request):
	return render(request,'generator/about.html')