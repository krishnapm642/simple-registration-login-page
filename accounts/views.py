from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
	if request.method == 'POST':
		uname = request.POST['name']
		try:
			user = User.objects.get(username = uname)
			return render(request, 'accounts/register.html',{'message':'Username already exist'})

		except User.DoesNotExist:
			user = User.objects.create_user(username =  request.POST['name'],password = request.POST['password'])
			return render(request, 'accounts/register.html',{'message':'user created'})
	else:
		return render(request, 'accounts/register.html',)

def login(request):
	if request.method == 'POST':
		uname = request.POST['name']
		pwd = request.POST['password']
		user = auth.authenticate(username = uname, password = pwd)
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'accounts/login.html',{'message' : "invalid credentials"})

	return render(request, 'accounts/login.html')

def home(request):
	return render(request, 'accounts/home.html')

@login_required
def logout(request):
	if request.method == "POST":
		auth.logout(request)
		return redirect('home')